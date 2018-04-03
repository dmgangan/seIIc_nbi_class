def cpe(data, backhaul = True):
    if backhaul:
        bh = { 'Backhauling': [
                    {'name': data['bhName'],
                     'cpeSideIPAddressSource': 'PROFILE',
                     'cpeSideIPAddressValue': None}]}
        bh_rtt = 'FROM_MANAGED_GROUP'

    else:
        bh = None
        bh_rtt = None

    cpe = {'cpe':{
        'cpeId': {
            'managedGroupId': data['managedGroupId'],
    		'subscriberId': data['subscriberId']
        },
        'getMacFromCPE': 'ENABLE',
        'clusterCode': data['clusterCode'],
        'platform': data['platform'],
        'ipStack': 'IPV4_ONLY',
        'subscriberPublicIPv6Address': None,
        'ipv6ConnectivityMode': None,
        'slaName': data['slaName'],
        'rtnClassifierName': data['rtnClassifierName'],
        'description': data['terminalName'],
        'authorization': 'TX_BLOCKED',
        'dataAuthorization': 'AUTHORIZED',
        'locationCode': None,
        'subscriberPublicIpAddress': None,
        'ipAddressing': 'ROUTER',
        'ipv4Prefix': None,
        'ipv4Dhcp': None,
        'provStatus': 'PRE_PROVISION',
        'autoGenerateResetQuota': 'ENABLE',
        'resetQuotaDay': '24',
        'resetQuotaTime': '2',
        'nicMode': None,
        'vrs': {
            'VR': [
                {
                    'vlanId': data['vlanId'],
                    'ipv4': {
                        'subscriberPublicIpAddress': data['IpAddress'],
                        'ipv4Prefix': data['ipv4Prefix'],
                        'ipv4Dhcp': 'DISABLE',
                        'natPrivateAddress': None
                    },
                    'ipv6': None,
                    'ipv4DynamicRoute': {
                        'satelliteRIPv2': 'BOTH',
                        'lanRIPv2': 'DISABLE',
                        'advertiseDGtoLAN': None,
                        'dgRIPv2HopCount': None
                    },
                    'ipv6DynamicRoute': None,
                    'enableBackhauling': 'SET_BY_MANAGED_GROUP',
                    'backhaulings': bh,
                    'enableGtp': None,
                    'gtp': None,
                    'vrrpMode': 'DISABLE',
                    'groupID': '1',
                    'groupIPAddress': None,
                    'priority': '100',
                    'advertisementInterval': '1',
                    'preempt': 'DISABLE',
                    'greAcceleration': 'ENABLE',
                    'transparency': 'DISABLE',
                    'reTagging': 'DISABLE',
                    'newVlanID': '10'
                }
            ]
        },
        'rfCertificationMode': '0',
        'minimumTxCoPolReceptionThreashold': '100',
        'minimumTxCoPolCn': '100',
        'coCrossPolDelta': '200',
        'minimumCpeRxEsNo': '30',
        'rttMeasurement': bh_rtt,
        'rtnScpcMode': None,
        'fwdTpLimit': '10',
        'scpcTpLimit': '0',
        'aes256Encryption': 'DISABLE',
        'httpAcceleration': 'DISABLE',
        'mobility': 'DISABLE',
        'longitude': None,
        'latitude': None,
        'mobilityParams': None,
        'greAcceleration': 'DISABLE',
        'mgMigration': None,
        'gtpAcceleration': 'DISABLE',
        'spspLicense': 'DISABLE',
        'mobilityType': None,
        'coordinatesSource': 'NO_COORDINATES'
    }}
    return cpe


def cpeId(data):
    cpeId = { 'cpeId': { 'managedGroupId': data['managedGroupId'],
                         'subscriberId': data['subscriberId']}}
    return cpeId

def cid(data):
    cid = {'id': { 'managedGroupId': data['managedGroupId'],
                  'subscriberId': data['subscriberId']}}
    return cid

def slaProfile(data):
    sla = {  'cpeId': { 'managedGroupId': data['managedGroupId'],
                        'subscriberId': data['subscriberId']},
             'slaName': data['slaName']}
    return sla

def rtnProfile(data):
    rtn = {  'cpeId': { 'managedGroupId': data['managedGroupId'],
                        'subscriberId': data['subscriberId']},
             'rtnClassifierName': data['rtnClassifierName']}
    return rtn

def cpeRoute(data):
    route = { 'cpeId': { 'managedGroupId': data['managedGroupId'],
                         'subscriberId': data['subscriberId']},
              'vlanId': data['vlanId'],
              'IPv4StaticRoute': {
                        'network':  data['routeNetwork'],
                        'subnetMask':  data['routeSubnetMask'],
                        'nextHop':  data['routeNextHop'],
                        'ipV4Interface': 'LAN',
                        'redistribute': 'RIPv2',
                        'distributedMetric': '1'}}
    return route

def bhProf(data):
    bh_prof = { 'cpeId': { 'managedGroupId': data['managedGroupId'],
                          'subscriberId': data['subscriberId']},
                'vlanIdToUpdate': data['vlanId'],
                'backhauling': {
                        'name': data['bhName'],
                        'cpeSideIPAddressSource': 'PROFILE',
                        'cpeSideIPAddressValue':None}}
    return bh_prof

def bhMode(data):
    bh_mode = { 'cpeId': { 'managedGroupId': data['managedGroupId'],
                          'subscriberId': data['subscriberId']},
                'vlanIdToUpdate': data['vlanId'],
                'vr':{  'vlanId':data['vlanId'],
                        'enableBackhauling':data['backhaulingState']}}
    return bh_mode

def custInfo(data):
    cust_info = {'customerInformation' : {
                    'cpeId': {  'managedGroupId': data['managedGroupId'],
                                'subscriberId': data['subscriberId']},
                    'cpeDescription': data['cpeDescription'],
                    'companyName': data['companyName'],
                    'companyGroupDivision': data['companyGroupDivision']}}
    return cust_info
