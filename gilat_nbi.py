from requests import Session
import requests, sys, gilat_nbi, nbi_conf, nbi_data
from requests.auth import HTTPBasicAuth
from zeep import *
from zeep.transports import Transport

class seiic(object):

    clinet = None
    nbi_session = None
    info_flash = None       #flash variable may be used to visualize exceptions in Flask web framework

    def __init__(self):
        self.nbi_session = requests.Session()
        self.nbi_session.auth = HTTPBasicAuth(nbi_conf.nbi_user, nbi_conf.nbi_pass)
        self.client = Client(nbi_conf.wsdl_filename,transport=Transport(session=self.nbi_session))

    def req(self, task, request_body):

        tasks={
            'cpeAddBHtoVR':{'reqst':'cpeAddBHtoVR'},
            'cpeDeleteBHfromVR':{'reqst':'cpeDeleteBHfromVR'},
            'cpeAddStaticRouteIPv4':{'reqst':'cpeAddStaticRouteIPv4'},
            'cpeDeleteStaticRouteIPv4':{'reqst':'cpeDeleteStaticRouteIPv4'},
            'cpeEnableBH':{'reqst':'cpeModifyVR'},
            'cpeDisableBH':{'reqst':'cpeModifyVR'},
            'cpeSetSLA':{'reqst':'modifyCPE'},
            'cpeSetRTN':{'reqst':'modifyCPE'},
            'createCPE':{'reqst':'createCPE'},
            'setCPECustomerInformation':{'reqst':'setCPECustomerInformation'},
            'getCPEbyID':{'reqst':'getCPEbyID'}
            }

        if task in tasks.keys():
            try:
                response = getattr(self.client.service, tasks[task]['reqst'])(**request_body)
                return ({'response':response, 'status': True})
            except exceptions.Fault as error:
                print (ValueError(error.message))
                return ({'response':request_body, 'status':False})
            except requests.exceptions.ConnectionError as http_error:
                print (ValueError(tasks[task]['reqst']+': Connection problem'))
                return ({'response':request_body, 'status': False})
            except:
                return ({'response':request_body, 'status': False})
                raise
                #print (ValueError(tasks[task]['reqst']+': Unexpected problem'))
        else:
            print ('Unknown task received: {}\nClosing...'.format(task))
            sys.exit()

    def cpeAddBHtoVR(self, bh_add_data):
        request = self.req('cpeAddBHtoVR', bh_add_data)
        return request

    def cpeDeleteBHfromVR(self, bh_del_data):
        request = self.req('cpeDeleteBHfromVR', bh_del_data)
        return request

    def cpeAddStaticRouteIPv4(self, rt_add_data):
        request = self.req('cpeAddStaticRouteIPv4', rt_add_data)
        return request

    def cpeDeleteStaticRouteIPv4(self, rt_del_data):
        request = self.req('deleteRoute', rt_del_data)
        return request

    def cpeEnableBH(self, vr_en_data):
        request = self.req('cpeEnableBH', vr_en_data)
        return request

    def cpeDisableBH(self, vr_ds_data):
        request = self.req('cpeDisableBH', vr_ds_data)
        return request

    def cpeSetSLA(self, sla_data):
        request = self.req('cpeSetSLA', sla_data)
        return request

    def cpeSetRTN(self, rtn_data):
        request = self.req('cpeSetRTN', rtn_data)
        return request

    def createCPE(self, cpe_data):
        request = self.req('createCPE', cpe_data)
        return request

    def setCPECustomerInformation(self, cust_data):
        request = self.req('setCPECustomerInformation', cust_data)
        return request

    def getCPEbyID(self, cid):
        response = self.req('getCPEbyID', cid)
        if response:
            return response
        else:
            return ('{} : no response'.format(cid['id']['subscriberId']))

    def getCPEsByManagedGroup(self,mg_id):
        cpesList=[]
        mg_data = {
                'managedGroupId': mg_id,
                'lastIndex':0,
            }
        cpesBulk = self.client.service.getCPEsByManagedGroup(**mg_data)
        cpesList += cpesBulk.cpes['CPE']
        while cpesBulk.hasMore:
            request_cpe['lastIndex']=cpesBulk.lastIndex
            cpesBulk = self.client.service.getCPEsByManagedGroup(**mg_data)
            cpesList += cpesBulk.cpes['CPE']
        return cpesList

def main():
    pass
if __name__ == '__main__':
    main()
