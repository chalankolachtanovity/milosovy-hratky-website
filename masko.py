from flask import Flask
import requests
from flask import Flask, request
from threading import Thread
import os

KMASKO = requests.get((os.getenv('t_kmaso')), auth=('user', 'pass'))

KMASKO = KMASKO.json()
masko_kills_teaser = []
masko_kills_knife = []
masko_kills = []
masko_hs_percentage = []
kmasko_kd_list = []
masko_deaths = []


def blue_square():
    with open("blue_square.html", "r") as f:
        htmll = f.read()
    return htmll


def kmasko_stat():
    kmaso = KMASKO['playerstats']['stats']
    for stat in kmaso:
        if stat['name'] == 'total_kills_knife':  # other stats
            total_kills_knife = stat['value']
        elif stat['name'] == 'total_kills':  # other stats
            total_kills = stat['value']
        elif stat['name'] == 'total_kills_taser':  # other stats
            total_kills_taser = stat['value']
        elif stat['name'] == 'total_kills_famas':
            total_kills_famas = stat['value']
        elif stat['name'] == 'total_kills_galilar':
            total_kills_galilar = stat['value']
        elif stat['name'] == 'total_kills_m4a1':
            total_kills_m4a1 = stat['value']
        elif stat['name'] == 'total_kills_ak47':
            total_kills_ak47 = stat['value']
        elif stat['name'] == 'total_kills_awp':
            total_kills_awp = stat['value']
        elif stat['name'] == 'total_kills_ssg08':
            total_kills_ssg08 = stat['value']
        elif stat['name'] == 'total_kills_aug':
            total_kills_aug = stat['value']
        elif stat['name'] == 'total_kills_sg556':
            total_kills_sg556 = stat['value']
        elif stat['name'] == 'total_kills_scar20':
            total_kills_scar20 = stat['value']
        elif stat['name'] == 'total_kills_g3sg1':
            total_kills_g3sg1 = stat['value']
        elif stat['name'] == 'total_kills_mac10':
            total_kills_mac10 = stat['value']
        elif stat['name'] == 'total_kills_mp9':
            total_kills_mp9 = stat['value']
        elif stat['name'] == 'total_kills_mp7':
            total_kills_mp7 = stat['value']
        elif stat['name'] == 'total_kills_ump45':
            total_kills_ump45 = stat['value']
        elif stat['name'] == 'total_kills_p90':
            total_kills_p90 = stat['value']
        elif stat['name'] == 'total_kills_bizon':
            total_kills_bizon = stat['value']
        elif stat['name'] == 'total_kills_negev':
            total_kills_negev = stat['value']
        elif stat['name'] == 'total_kills_mag7':
            total_kills_mag7 = stat['value']
        elif stat['name'] == 'total_kills_glock':
            total_kills_glock = stat['value']
        elif stat['name'] == 'total_kills_p250':
            total_kills_p250 = stat['value']
        elif stat['name'] == 'total_kills_tec9':
            total_kills_tec9 = stat['value']
        elif stat['name'] == 'total_kills_fiveseven':
            total_kills_fiveseven = stat['value']
        elif stat['name'] == 'total_damage_done':
            total_damage_done = stat['value']
        elif stat['name'] == 'total_planted_bombs':
            total_planted_bombs = stat['value']
        elif stat['name'] == 'total_defused_bombs':
            total_defused_bombs = stat['value']
        elif stat['name'] == 'total_kills':
            total_kills = stat['value']
        elif stat['name'] == 'total_kills_headshot':
            total_kills_headshot = stat['value']
        elif stat['name'] == 'total_deaths':
            total_deaths = stat['value']
        elif stat['name'] == 'total_wins':
            total_wins = stat['value']
    kd_kmasko = total_kills / total_deaths
    if kd_kmasko not in kmasko_kd_list:
        kmasko_kd_list.append(kd_kmasko)
    hs_masko = total_kills_headshot * 100 / total_kills
    hs_masko = int(hs_masko)
    if hs_masko not in masko_hs_percentage:
        masko_hs_percentage.append(hs_masko)
    if total_kills_knife not in masko_kills_knife:
        masko_kills_knife.append(total_kills_knife)
    if total_kills_taser not in masko_kills_teaser:
        masko_kills_teaser.append(total_kills_taser)
    if total_kills not in masko_kills:
        masko_kills.append(total_kills)
    if total_deaths not in masko_deaths:
        masko_deaths.append(total_deaths)

    return (f""" 
  <html>
      <link rel="icon" href="https://dam.nmhmedia.sk/image/3d61f2ee-e9cc-4f0d-9fea-d1f5b82bb61b_dam-urlwlvhbz.jpg/960/540">
      <body>
        <title>Kmaaaaaaaaaaaaaaaaasko</title>
         <h1>Kmáskové štatistiky</h1>
        {blue_square()}
      </body>
  <body style = "font-family: Verdana, sans-serif;">    
    <table>
      <p style = "font-family:courier,arial,helvetica;">
        <tr><td>Total kills:</td><td>| {total_kills} |</td>
          <tr><td>Total deaths:</td><td>| {total_deaths} |</td>
            <tr><td>Total wins:</td><td>| {total_wins} |</td>
          <tr><td>Total demage done:</td><td>| {total_damage_done} |</td>
          <tr><td>Total planted bombs:</td><td>| {total_planted_bombs} |</td>
        <tr><td>Total defused bombs:</td><td>| {total_defused_bombs} |</td>
    </table>
    {blue_square()}
    <table>
      <h3>Rifles</h3>
        <tr><td>Total kills FAMAS:</td><td>| {total_kills_famas} |--</td><td>|VS|-- Total kills Galil:</td><td>| {total_kills_galilar} |</td>
          <tr><td>Total kills M4A1:</td><td>| {total_kills_m4a1} |--</td><td>|VS|-- Total kills AK-47:</td><td>| {total_kills_ak47} |</td><div> 
            <tr><td>Total kills AWP:</td><td>| {total_kills_awp} |--</td><td>|VS|-- Total kills SCOUT:</td><td>| {total_kills_ssg08} |</td>
          <tr><td>Total kills AUG:</td><td>| {total_kills_aug} |--</td><td>|VS|-- Total kills SG556:</td><td>| {total_kills_sg556} |</td>
        <tr><td>Total kills LAMA CT:</td><td>| {total_kills_scar20} |--</td><td>|VS|-- Total kills LAMA T:</td><td>| {total_kills_g3sg1} |</td>
    </table>
    {blue_square()}
    <table>
      <h3>SMG's</h3>
        <tr><td>Total kills MAC-10:</td><td>| {total_kills_mac10} |--</td><td>|VS|-- Total kills MP9:</td><td>| {total_kills_mp9} |</td>
          <tr><td>Total kills MP-7:</td><td>| {total_kills_mp7} |</td>
            <tr><td>Total kills UMP-45:</td><td>| {total_kills_ump45} |</td>
          <tr><td>Total kills P90:</td><td>| {total_kills_p90} |</td>
        <tr><td>Total kills BIZON:</td><td>| {total_kills_bizon} |</td>
    </table>
    {blue_square()}
    <table>
      <h3>Heavy</h3>
        <tr><td>Total kills NEGEV:</td><td>| {total_kills_negev} |</td> 
        <tr><td>Total kills MAG-7:</td><td>| {total_kills_mag7} |</td> 
    </table>  
    {blue_square()}
    <table>  
      <h3>Pistols</h3>
        <tr><td>Total kills GLOCK-18:</td><td>| {total_kills_glock} |</td>
          <tr><td>Total kills P250:</td><td>| {total_kills_p250} |</td>
        <tr><td>Total kills TEC-9:</td><td>| {total_kills_tec9} |--</td><td>|VS|-- Total kills FIVESEVEN:</td><td>| {total_kills_fiveseven} |</td>
    </table>
  </body>
  <img src="https://www.sports.sk/Data/1092/UserFiles/clanky/sona_predna_sumce/sumec_1.png" width="100%" height="20%">
  </html>
  """)
