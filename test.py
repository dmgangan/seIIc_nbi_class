import gilat_nbi, nbi_conf, nbi_data, pprint, sys, datetime, m_options
from pprint import pprint

def main():
    #get_by_id_data = {'managedGroupId': 2,'subscriberId': 1018}
    options = m_options.opts(sys.argv[1:])
    now = datetime.datetime.now()
    vsat = gilat_nbi.seiic()

    cpe_fail = []
    rt_fail = []
    bh_fail = []
    inf_fail = []
    cpe_succ = []
    rt_succ = []
    bh_succ = []
    inf_succ = []

    with open(nbi_conf.vsat_table_name, 'r') as m:
        csv = m.read()

    title = csv.splitlines()[0].split(',')

    for line in csv.splitlines()[1:]:
        data = dict(zip(title,line.split(',')))

        bh = False
        rt = False
        if (data['bhName'] and options['backhaul']): bh = True
        if (options['route'] and data['routeNetwork'] and data['routeNetwork'] and data['routeNetwork']): rt = True

        if options['create']:
            print ('\n{:5} CPE:{:5}'.format(now.strftime("%H:%M:%S"),data['subscriberId']))
            if options['debug']: pprint (nbi_data.cpe(data, bh))
            addcpe = vsat.createCPE(nbi_data.cpe(data, bh))
            if addcpe['status']:
                print('  --> [{}] CPE created'.format(data['subscriberId']))
                cpe_succ.append(data['subscriberId'])
                if options['backhaul']:
                    if bh:
                        print('  --> [{}] Backhauling assigned'.format(data['subscriberId']))
                        bh_succ.append(data['subscriberId'])
                    else:
                        print('  --x [{}] BH skipped! (not present in .csv)'.format(data['subscriberId']))
                        bh_fail.append(data['subscriberId'])
            else:
                print('  --x [{}] CPE create failed!'.format(data['subscriberId']))
                cpe_fail.append(data['subscriberId'])

        if (not options['create'] and options['backhaul']):
            if bh:
                if options['debug']: pprint (nbi_data.bhProf(data))
                addbh = vsat.cpeAddBHtoVR(nbi_data.bhProf(data))
                if addbh['status']:
                    print('  --> [{}] Backhauling assigned'.format(data['subscriberId']))
                    bh_succ.append(data['subscriberId'])
                else:
                    print('  --x [{}] Backhauling assign failed!'.format(data['subscriberId']))
                    bh_fail.append(data['subscriberId'])
            else:
                print('  --x [{}] BH skipped! (not present in .csv)'.format(data['subscriberId']))

        if options['route']:
            if rt:
                if options['debug']: pprint (nbi_data.cpeRoute(data))
                addrt = vsat.cpeAddStaticRouteIPv4(nbi_data.cpeRoute(data))
                if addrt['status']:
                    print('  --> [{}] Route added'.format(data['subscriberId']))
                    rt_succ.append(data['subscriberId'])
                else:
                    print('  --x [{}] Route add failed!'.format(data['subscriberId']))
                    rt_fail.append(data['subscriberId'])
            else:
                print('  --x [{}] Route skipped! (not present in .csv)'.format(data['subscriberId']))

        if options['info']:
            if options['debug']: pprint (nbi_data.custInfo(data))
            addinf = vsat.setCPECustomerInformation(nbi_data.custInfo(data))
            if addinf['status']:
                print('  --> [{}] Info added'.format(data['subscriberId']))
                inf_succ.append(data['subscriberId'])
            else:
                print('  --x [{}] Info add failed!'.format(data['subscriberId']))
                inf_fail.append(data['subscriberId'])



    if options['create']:
        print ('\n{}\nCPEs:\n\tSUCCESS: {}\n\tFAILURE: {} -> {}'.format('-'*23,len(cpe_succ),len(cpe_fail),cpe_fail))

    if options['route']:
        print ('ROUTE:\n\tSUCCESS: {}\n\tFAILURE: {} -> {}'.format(len(rt_succ),len(rt_fail),rt_fail))

    if options['backhaul']:
        print ('BACKHAUL:\n\tSUCCESS: {}\n\tFAILURE: {} -> {}'.format(len(bh_succ),len(bh_fail),bh_fail))

    if options['info']:
        print ('INFO:\n\tSUCCESS: {}\n\tFAILURE: {} -> {}'.format(len(inf_succ),len(inf_fail),inf_fail))


if __name__ == '__main__':
    main()
