def cpe(data):
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
                    'backhaulings': {
                            'Backhauling': [
                                {
                                    'name': data['bhName'],
                                    'cpeSideIPAddressSource': 'PROFILE',
                                    'cpeSideIPAddressValue': None
                                }
                            ]
                        },
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
        'rttMeasurement': 'FROM_MANAGED_GROUP',
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
