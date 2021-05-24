import configparser
import pygame.locals

DEFAULT ={
    'Audio':{
        'samplerate' : 48000
    },
    'Keymaps': {
        'key_stop' : 'K_1',
        'key_record' : 'K_2',
        'key_play' : 'K_3',
        'key_overdub' : 'K_4'
    }
}

def config_read():
    #read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    if not config.has_section('Audio'):
        config.read_dict(DEFAULT)
        with open('config.ini', 'w') as audiofile:
            config.write(audiofile)
        return config
    #confirm config file sction
    if not config_check(config):
        config.read_dict(DEFAULT)
    return config

def config_check(config):
    #read section
    try:
        for k, v in config.items('Keymaps'):
            getattr(pygame.locals, v)
        config.getint('Audio', 'samplerate')
    except:
        return False
    return True
