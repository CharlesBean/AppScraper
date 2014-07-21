__author__ = 'charles.bean'

# from main.com.appscraper.src.playstore.data.information import Information
from main.com.appscraper.src.playstore.data.populator import Populator

def main():
	"""
	Runner

	"""
	populator = Populator()

	#results = populator.searchAPI('ford')

	results = [{'itemID': 'com.ford.remoteaccess', 'category': 'Ford Motor Co.', 'title': 'Ford Remote Access', 'price': 'Free'}, {'itemID': 'com.ciright.ford', 'category': 'GoMoto Inc', 'title': 'Ford Drive', 'price': 'Free'}, {'itemID': 'com.dragracingtunes', 'category': 'Igol corp.', 'title': 'Drag Racing World Record Tunes', 'price': 'Free'}, {'itemID': 'com.telenav.app.android.scout_us', 'category': 'Telenav, Inc.', 'title': 'Scout GPS Navigation & Traffic', 'price': 'Free'}, {'itemID': 'OCTech.Mobile.Applications.OBDLink', 'category': 'ScanTool.net, LLC', 'title': 'OBDLink (OBD car diagnostics)', 'price': 'Free'}, {'itemID': 'com.ford.myfordtouchguide', 'category': 'Ford Motor Co.', 'title': 'MyFord Touch Guide', 'price': 'Free'}, {'itemID': 'com.threedpros.ford', 'category': 'Digital Panorama Inc.', 'title': 'Ford Türkiye', 'price': 'Free'}, {'itemID': 'ford.mustanglwp', 'category': 'Ford Motor Co', 'title': 'Ford Mustang Custom Wallpaper', 'price': 'Free'}, {'itemID': 'inrix.android.fordui', 'category': 'INRIX, Inc.', 'title': 'Ford SYNC® Destinations', 'price': 'Free'}, {'itemID': 'com.e180.fordmobile', 'category': 'Ford Argentina', 'title': 'Ford Mobile', 'price': 'Free'}, {'itemID': 'com.ford.mfm', 'category': 'Ford Motor Co.', 'title': 'MyFord Mobile', 'price': 'Free'}, {'itemID': 'com.ford.racing.ppcatalog', 'category': 'Ford Motor Co.', 'title': 'Ford Racing Parts Catalog', 'price': 'Free'}, {'itemID': 'com.goodwallpapers.tapety_ford', 'category': 'Best of the best', 'title': 'Ford wallpapers', 'price': 'Free'}, {'itemID': 'com.ford.atfordnews', 'category': 'Ford Motor Co.', 'title': '@Ford News', 'price': 'Free'}, {'itemID': 'com.lwpsystems.ford.mustang.shelby.clock.lwp', 'category': 'LWP Systems', 'title': 'Ford Mustang Shelby Clock LWP', 'price': 'Free'}, {'itemID': 'lt.mb.PlayFord', 'category': 'Aloris', 'title': 'FORD In My Pocket', 'price': 'Free'}, {'itemID': 'ru.av_projects.ff2manual', 'category': 'av_projects', 'title': 'Ремонт Ford Focus 2', 'price': 'Free'}, {'itemID': 'com.archapps.fordf150', 'category': 'AutoImmagini.com', 'title': 'Ford F150 Wallpapers', 'price': 'Free'}, {'itemID': 'com.neutronikart.ford', 'category': 'Neutronik ART', 'title': 'Ford Mustang', 'price': 'Free'}, {'itemID': 'com.cutewp.ford', 'category': 'Beautiful Wallpapers Group', 'title': 'Ford HD wallpapers', 'price': 'Free'}, {'itemID': 'com.tapatalk.fordownersclubcomforums', 'category': 'Auto Clubs International', 'title': 'Ford OC', 'price': 'Free'}, {'itemID': 'pl.mk2.fordfocus', 'category': 'pltedev', 'title': 'Ford Focus', 'price': 'Free'}, {'itemID': 'arch.mustang.wallpaper', 'category': 'AutoImmagini.com', 'title': 'Ford Mustang Wallpapers', 'price': 'Free'}, {'itemID': 'com.fordrangerforum.forumrunner', 'category': 'Tom C', 'title': 'Ford Ranger Forum App', 'price': 'Free'}, {'itemID': 'com.fordqr', 'category': 'Joker Mobile', 'title': 'Ford Lector QR', 'price': 'Free'}, {'itemID': 'mkmy.ppackage.namespace', 'category': 'pltedev', 'title': 'ford mondeo', 'price': 'Free'}, {'itemID': 'com.besttopgameswallpooo.fordfairlanegtgta', 'category': 'TopGamesWallpo', 'title': 'Ford Fairlane GTA', 'price': 'Free'}, {'itemID': 'com.coleccionford', 'category': 'Ford Motor Co.', 'title': 'Ford Collection', 'price': 'Free'}, {'itemID': 'com.a44396949351cc215d590b36a.a60633834a', 'category': 'TW Apps', 'title': 'Ford GT', 'price': 'Free'}, {'itemID': 'com.ford.catalogos', 'category': 'Ford Argentina', 'title': 'Ford Catálogos', 'price': 'Free'}, {'itemID': 'uk.co.fourteengreen.fordradiocodes', 'category': 'FourteenGreen', 'title': 'Ford Radio Codes', 'price': 'Free'}, {'itemID': 'com.ford.edge', 'category': 'Briabe Mobile, Inc.', 'title': 'Ford Edge Mobile Experience', 'price': 'Free'}, {'itemID': 'com.wetooo', 'category': 'Weto', 'title': 'Ford Mustangs Overview', 'price': 'Free'}, {'itemID': 'MustangsEEI.com', 'category': 'Oxegen Entertainment LLC.', 'title': 'Ford Mustang EXPOSED!', 'price': 'Free'}, {'itemID': 'thinkbig.cars.ford', 'category': 'Think BIG Pty Ltd', 'title': 'Ford', 'price': '$1.03'}, {'itemID': 'com.tyrellmedia.fordmustangwallpaper', 'category': 'Tyrell Media', 'title': 'Ford Mustang Wallpaper', 'price': 'Free'}, {'itemID': 'mustang.com', 'category': 'WebMobileTechnologies', 'title': 'Ford Mustang Wallpapers HD', 'price': 'Free'}, {'itemID': 'tw.com.ford.autonet', 'category': 'E-AutoNet Publication Taiwan', 'title': 'FORD News', 'price': 'Free'}, {'itemID': 'com.gearboxz.dtcs.ford64', 'category': 'Gear Box Z Inc', 'title': 'Ford Super Duty DTCs Free', 'price': 'Free'}, {'itemID': 'com.automotiontv.phillongfordofmotorcity', 'category': 'AutoMotionTV', 'title': 'Ford Motor City', 'price': 'Free'}, {'itemID': 'com.ZiminAdrian.FordFiestaWallpapers', 'category': 'Zimin Adrian', 'title': 'Ford Fiesta Wallpapers', 'price': 'Free'}, {'itemID': 'com.krdsmob.drivesmart', 'category': 'KRDS', 'title': 'Ford - Drive Smart', 'price': 'Free'}, {'itemID': 'com.ford.android.autoshow.naias2013', 'category': 'Imagination Ltd', 'title': 'Ford at NAIAS 2013', 'price': 'Free'}, {'itemID': 'com.camalotdesigns.fordmustangwallpaper', 'category': 'Ryan Conrad', 'title': 'Ford Mustang Wallpaper', 'price': '$0.99'}, {'itemID': 'com.singularity.fordecosportbd', 'category': 'Singularity', 'title': 'Ford AR', 'price': 'Free'}, {'itemID': 'com.a67259670851fea0e4dbb2c0a.a04585175a', 'category': 'Carin Jones', 'title': 'Ford Mustang Fan', 'price': 'Free'}, {'itemID': 'com.myaccessbox.scford', 'category': 'Autoninja', 'title': 'SC Ford Accessbox', 'price': 'Free'}, {'itemID': 'com.fordf150forum.forumrunner', 'category': 'Tom C', 'title': 'Ford F150 Forum App', 'price': 'Free'}]

	populator.populateApps(results)


if __name__ == '__main__':
	main()