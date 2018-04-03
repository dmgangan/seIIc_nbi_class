import getopt

def opts(argv):
    backhaul = False
    info = False
    route = False
    create = False
    debug = False
    
    opts, args = getopt.getopt(argv, 'birctd',['route','info','backhauling','create','test','debug'])
    for opt, arg in opts:
        if opt in ('-b','--backhauling'):
            backhaul = True
        if opt in ('-i','--info'):
            info = True
        if opt in ('-r','--route'):
            route = True
        if opt in ('-c','--create'):
            create = True
        if opt in ('--debug'):
            debug = True

    return {'create':create,'backhaul':backhaul,'info':info,'route':route, 'debug':debug}
