#coding=utf-8
'''
Powered By:ChongRui
web-fingerprint plugin
1. robots.txt detecting
2. Powered by DedeCMS detecting
'''
matches = {
	'robots':["Disallow: /plus/feedback_js.php",
			  "Disallow: /plus/mytag_js.php",
			  "Disallow: /plus/rss.php",
			  "Disallow: /plus/search.php",
			  "Disallow: /plus/recommend.php",
			  "Disallow: /plus/stow.php",
			  "Disallow: /plus/count.php"],
	'intext':[r'DedeCMS.*?']
}