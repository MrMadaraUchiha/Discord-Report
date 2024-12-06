"""
Script: DiscordReport
Author: [UBGE] DiaZ
Description: A simple script who allow a player to send a Report message in-game Directly to one or more Discord Channel/Server
-----------
Remember to Modify the ROLE_MENTION & WEBHOOK_URL TO THIS SCRIPT WORK PROPERLY
Command: /report <#ID/Nickname> <Message>
Comando: /reportar <#ID/Nickname> <Mensagem>
"""

import urllib
import urllib2,cookielib
import thread
from commands import add, name, get_player, join_arguments, alias
from pyspades.constants import *
from pyspades.server import *

USER_AGENT2 = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
WEBHOOK_URL = "WEBHOOK_URL_HERE"
LANGUAGE = "EN" #PT/EN
ROLE_MENTION = "<@!ID_NUMBER_HERE>" #Discord role Mention ID (Optional) FORMAT: <@!ID_NUMBER_HERE>
# url = "https://www.example.com"
# urllib.urlopen(url)

@name('report')
@alias("reportar")
def report(connection, value, *arg):
    #Declaration of Pysnip Constants and Variables
    player = get_player(connection.protocol, value)
    message = join_arguments(arg)
    player_name = player.name
    protocol = connection.protocol
    
    if LANGUAGE is "PT":
    
        reportmsg = "**%s** esta reportando o player: **%s**.\n**Motivo**: %s.\n**Servidor**: %s.\nIP: %s\n%s" % (connection.name, player_name, message, protocol.name, protocol.identifier, ROLE_MENTION)
        if not message:
            return "Digite a mensagem no seguinte formato: /reportar <#ID/Nickname> <Mensagem>"
        try:
            url=WEBHOOK_URL
            data = urllib.urlencode({"content": reportmsg})
            post_request = urllib2.Request(url, data)
            post_request.add_header("User-Agent", USER_AGENT)
            urllib2.urlopen(post_request).read()
        except:
            return "UMA EXCECAO OCORREU!!!"
        return 'O report foi enviado com Sucesso para a Equipe STAFF'
            
    elif LANGUAGE is "EN":
        
        reportmsg = "**%s** is reporting player: **%s**.\n**Reason**: %s.\n**Server**: %s.\nIP: %s\n%s" % (connection.name, player_name, message, protocol.name, protocol.identifier, ROLE_MENTION)
        if not message:
            return "Type the command in the following Format: Command: /report <#ID/Nickname> <Message>"
        try:
            url=WEBHOOK_URL
            data = urllib.urlencode({"content": reportmsg})
            post_request = urllib2.Request(url, data)
            post_request.add_header("User-Agent", USER_AGENT)
            thread.start_new_thread(urllib2.urlopen(post_request).read())
        except:
            return "A exception has occurred!"
        return 'The report has successfully sended to Staff Team'
add(report)
def apply_script(protocol, connection, config):


    class SendReportClass(connection):
    
# WILL BE IMPLEMENTED IN A FUTURE RELEASE
        def send_report(connection, message, url):
            url=WEBHOOK_URL
            data = urllib.urlencode({"content": message})
            post_request = urllib2.Request(url, data)
            post_request.add_header("User-Agent", USER_AGENT)
            thread.start_new_thread(urllib2.urlopen(post_request).read())
            return connection.enviar_report
    return protocol, SendReportClass
