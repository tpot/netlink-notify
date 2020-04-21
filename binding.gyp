{
	"targets": [
		{
			"target_name": "netlink_worker",
			"sources": [ "netlink.cpp" ], 
			"cflags": ["-Wall", "-std=c++11"],
			"cflags_cc": ["-Wall", "-std=c++11"],
			"cflags!": [ "-fno-exceptions" ],
			"cflags_cc!": [ "-fno-exceptions" ],
			"ldflags": ["-std=c++11"],
			"link_settings": { "libraries": ["-lmnl"] },
			"include_dirs" : [
				"<!(node -e \"require('nan')\")", 
				"<!(node -e \"require('streaming-worker-sdk')\")"
			]
		}
	]
}
