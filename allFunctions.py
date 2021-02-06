from aligator import *
from masko import *
from stano import *
from tajmoti import *
from teetou import *

hs_list = []
kd_list = []
stano_stat()
aligator_stat()
kmasko_stat()
teetou_stat()
tajmoti_stat()


def best_kd_ratio():
    kd_list.append(stano_kd_list)
    kd_list.append(aligator_kd_list)
    kd_list.append(kmasko_kd_list)
    kd_list.append(tajmoti_kd_list)
    kd_list.append(teetou_kd_list)
    best_kd = max(kd_list)
    return (f"""
    <html>
        <link rel="icon" href="https://preview.redd.it/lh72f11p5jo31.png?auto=webp&s=c7252a6eeffdb5cdec87726552bac678667d95a5">
        <body>
            <title>K/D ratio</title>
          <h2>K/D ratio Lachtanov</h2>
        </body>
      <body style = "font-family: Verdana, sans-serif;">
        <table>
          <tr><td>Stano k/d:</td><td>| {stano_kd_list[0]} |</td>
            <tr><td>Aligator k/d:</td><td>| {aligator_kd_list[0]} |</td>
              <tr><td>Kmaso k/d:</td><td>| {kmasko_kd_list[0]} |</td>
            <tr><td>Teetou k/d:</td><td>| {teetou_kd_list[0]} |</td>
          <tr><td>Tajmoti k/d:</td><td>| {tajmoti_kd_list[0]} |</td>
        </table>
          <img src="https://6.viki.io/image/7e05fe5b86b642c783dbbe1eeb92fd93.jpeg?s=900x600&e=t" alt="HTML5 Icon" width="25%" height="15%">
          <body>
            <h4>Best k/d ratio is: {best_kd[0]}</h4>
          </body>
        <body>
          <h3>Kartička pre idiotov:</h3>
            <table border=3>
              <tr><td>KD = kills / deaths , for your kill/deaths ratio; and. That means, if a<br> player has 10 kills and 5 deaths, his KD ratio is equal to 2. A KD ratio of 1 means<br> that the player got killed exactly as many times as he successfully eliminated his<br> opponents.
            </tr></td>
          </body>
        </table>
      </body>
    </html>
  """)


def h_percentage():
    hs_list.append(stano_hs_percentage)
    hs_list.append(aligator_hs_percentage)
    hs_list.append(masko_hs_percentage)
    hs_list.append(tajmoti_hs_percentage)
    hs_list.append(teetou_hs_percentage)
    new_list = [str(inner_list[0]) for inner_list in (hs_list)]
    hs_max = max(new_list)
    return (f"""
  <html>
    <link rel="icon" href="https://seeklogo.com/images/C/csgo-headshot-logo-D55BFE7334-seeklogo.com.png">
      <body>
          <title>H/S ratio</title>
        <h2>H/S ratio Lachtanov</h2>
      </body>
    <table>
      <body style = "font-family: Verdana, sans-serif;">
        <tr><td>Stano ratio:</td><td>| {stano_hs_percentage[0]}% |</td>
          <tr><td>Aligator ratio:</td><td>| {aligator_hs_percentage[0]}% |</td>
            <tr><td>Kmaso ratio:</td><td>| {masko_hs_percentage[0]}% |</td>
          <tr><td>Teetou ratio:</td><td>| {teetou_hs_percentage[0]}% |</td>
        <tr><td>Tajmoti ratio:</td><td>| {tajmoti_hs_percentage[0]}% |</td>
    </table>
      <img src="https://staging2.filmdaily.co/wp-content/uploads/2020/05/coughing-cat-meme-lede.jpg" alt="HTML5 Icon" width="25%" height="20%">
        <h4>Best H/S ratio is: {hs_max}%</h4>
      <p1>stano ty zmrd</p1>
    </body>
  </html>
  """)


def other_stats():
    return (f"""
  <html>
    <link rel="icon" href="https://cdn3.iconfinder.com/data/icons/e-commerce-8/91/stats-512.png">
      <body>
          <title>Other stats</title>
        <h1><u>Other stats</u></h1>
      </body>
    <table>
      <h3>Total kills</h3>
        <body style = "font-family: Verdana, sans-serif;">
          <tr><td>Stano total kills</td><td>| {stano_kills[0]} |---</td><td>|D|---| {stano_deaths[0]} |</td>
            <tr><td>Aligator total kills</td><td>| {aligator_kills[0]} |---</td><td>|D|---| {aligator_deaths[0]} |</td>
            <tr><td>Kmaso total kills</td><td>| {masko_kills[0]} |---</td><td>|D|---| {masko_deaths[0]} |</td>
          <tr><td>Teetou total kills</td><td>| {teetou_kills[0]} |---</td><td>|D|---| {teetou_deaths[0]} |</td>
        <tr><td>Tajmoti total kills</td><td>| {tajmoti_kills[0]} |---</td><td>|D|---| {tajmoti_deaths[0]} |</td>
    </table>
    {blue_square()}
    <table>
      <h3>Total knife kills</h3>
        <body style = "font-family: Verdana, sans-serif;">
          <tr><td>Stano knife kills</td><td>| {stano_kills_knife[0]} |</td>
            <tr><td>Aligator knife kills</td><td>| {aligator_kills_knife[0]} |</td>
            <tr><td>Kmaso knife kills</td><td>| {masko_kills_knife[0]} |</td>
          <tr><td>Teetou knife kills</td><td>| {teetou_kills_knife[0]} |</td>
        <tr><td>Tajmoti knife kills</td><td>| {tajmoti_kills_knife[0]} |</td>
    </table>
    {blue_square()}
    <table>
      <h3>Total TASER kills</h3>
        <body style = "font-family: Verdana, sans-serif;">
          <tr><td>Stano TASER kills</td><td>| {stano_kills_teaser[0]} |</td>
            <tr><td>Aligator TASER kills</td><td>| {aligator_kills_teaser[0]} |</td>
            <tr><td>Kmaso TASER kills</td><td>| {masko_kills_teaser[0]} |</td>
          <tr><td>Teetou TASER kills</td><td>| 0 |</td>
        <tr><td>Tajmoti TASER kills</td><td>| {tajmoti_kills_teaser[0]} |</td>
    </table>
    <img src="https://cdn.countryflags.com/thumbs/russia/flag-400.png" width="100%" height="33%">
    </body>
  </html>
  """)
