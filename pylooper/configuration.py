import configparser

DEFAULT ={
    'title' : 'Looper',
    'volume' : '50',
    'stop' : 'K_1',
    'record' : 'K_2',
    'play' : 'K_3',
    'overdub' : 'K_4',
    'samplerate' : '48000'}

def config_generator():
    #make config file
    config = configparser.ConfigParser()

    # make config object
    config['audio'] = DEFAULT
    

    #save config file
    with open('audio.ini', 'w') as audiofile:
        config.write(audiofile)

def config_read():
    #read config file
    config = configparser.ConfigParser()
    try:
        config.read('audio.ini')
    except FileNotFoundError:
        config_generator()
    else:
        #confirm config file sction
        config.sections()
        ini_read(config)

def ini_read(config):
    #read section
    title = config['audio']['title']
    volume = config['audio']['volume']
    stop = config['audio']['stop']
    record = config['audio']['record']
    play = config['audio']['play']
    overdub = config['audio']['overdub']
    samplerate = config['audio']['samplerate']

config_generator()
config_read()
