{
	'variables':{
		'library' : 'static_library',
		#'library' : 'shared_library',
		'yasm_flags':[],
	},
	'target_defaults': {
		'defines':[	
		],
		'include_dirs':[
			'config',
			'v4l-utils_src/include',
		],
		'direct_dependent_settings': {
			'include_dirs': [
				'v4l-utils_src/include',
			],
		 },
		
		
		'conditions': [
		  ['OS != "win"', {
			'defines': [
			  '_LARGEFILE_SOURCE',
			  '_FILE_OFFSET_BITS=64',
			],
			'conditions': [
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'cflags': [ '-pthread' ],
			  }],
			  ['library == "shared_library"',{
				'cflags':[
					'-fPIC',
				],
			  }],
			],
		}],
		['OS=="android"',{
			'include_dirs':[
				#'config/android'
			],
			'defines':[
				'ANDROID'
			],
		  }],
		],
	  },
	'targets':
	[
		{
			'target_name': 'v4l2',
			'type':'<(library)',

			'include_dirs':[
				'v4l-utils_src/lib/include',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'v4l-utils_src/include',
					'v4l-utils_src/lib/include',
				],
			 },
			'sources':[
				
			],
		},
		{
			'target_name': 'libv4l2',
			'type':'<(library)',
			'dependencies':[
				'../libglob.module/libglob.gyp:libglob',
				'libv4lconvert',
			],
			'defines':[],
			'include_dirs':[
				'v4l-utils_src/lib/include',
				'v4l-utils_src',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'v4l-utils_src/lib/include'
				],
			 },
			 
			 'conditions':[
				 ['OS == "linux"',{
					'link_settings':{
						'libraries':[
							'-ldl',
							'-lrt',
						],
					},
				}],
			],
			 
			'sources':[
				'v4l-utils_src/lib/libv4l2/libv4l2.c',
				'v4l-utils_src/lib/libv4l2/v4l2-plugin.c',
				'v4l-utils_src/lib/libv4l2/log.c',
				'v4l-utils_src/lib/libv4l2/libv4l2-priv.h',
				#'v4l-utils_src/lib/libv4l2/v4l2convert.c',
			],
		},
		
		{
			'target_name': 'libv4lconvert',
			'type':'<(library)',
			'dependencies':[
				'../libjpeg-turbo.module/libjpeg.gyp:libjpeg',
			],
			'defines':[],
			'include_dirs':[
				'v4l-utils_src/lib/include',
				'v4l-utils_src',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'v4l-utils_src/lib/include',
					'v4l-utils_src/',
				],
			 },
			 
			'sources':[
				'v4l-utils_src/lib/libv4lconvert/libv4lconvert.c',
				'v4l-utils_src/lib/libv4lconvert/bayer.c',
				'v4l-utils_src/lib/libv4lconvert/cpia1.c',
				'v4l-utils_src/lib/libv4lconvert/crop.c',
				'v4l-utils_src/lib/libv4lconvert/flip.c',
				'v4l-utils_src/lib/libv4lconvert/helper.c',
				'v4l-utils_src/lib/libv4lconvert/hm12.c',
				'v4l-utils_src/lib/libv4lconvert/jidctflt.c',
				'v4l-utils_src/lib/libv4lconvert/jl2005bcd.c',
				'v4l-utils_src/lib/libv4lconvert/jpeg.c',
				'v4l-utils_src/lib/libv4lconvert/jpeg_memsrcdest.c',
				'v4l-utils_src/lib/libv4lconvert/jpgl.c',
				'v4l-utils_src/lib/libv4lconvert/mr97310a.c',
				#'v4l-utils_src/lib/libv4lconvert/ov511-decomp.c',
				#'v4l-utils_src/lib/libv4lconvert/ov518-decomp.c',
				'v4l-utils_src/lib/libv4lconvert/pac207.c',
				'v4l-utils_src/lib/libv4lconvert/rgbyuv.c',
				'v4l-utils_src/lib/libv4lconvert/se401.c',
				'v4l-utils_src/lib/libv4lconvert/sn9c10x.c',
				'v4l-utils_src/lib/libv4lconvert/sn9c2028-decomp.c',
				'v4l-utils_src/lib/libv4lconvert/sn9c20x.c',
				'v4l-utils_src/lib/libv4lconvert/spca501.c',
				'v4l-utils_src/lib/libv4lconvert/spca561-decompress.c',
				'v4l-utils_src/lib/libv4lconvert/sq905c.c',
				'v4l-utils_src/lib/libv4lconvert/stv0680.c',
				'v4l-utils_src/lib/libv4lconvert/tinyjpeg.c',
				'v4l-utils_src/lib/libv4lconvert/control/libv4lcontrol.c',
				'v4l-utils_src/lib/libv4lconvert/processing/autogain.c',
				'v4l-utils_src/lib/libv4lconvert/processing/gamma.c',
				'v4l-utils_src/lib/libv4lconvert/processing/libv4lprocessing.c',
				'v4l-utils_src/lib/libv4lconvert/processing/whitebalance.c',
			],
			'conditions':[
				['OS == "android"',{
					'sources':[
						'config/android-config.c',
					],
				}],
			],
		},
		
		{
			'target_name': 'v4l2-ctl',
			'type':'executable',
			'dependencies':[
				'libv4l2'
			],
			'defines':[],
			'include_dirs':[
				'v4l-utils_src',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'v4l-utils_src',
				],
			 },
			 
			 
			'sources':[
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl.h',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-common.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-tuner.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-io.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-stds.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-vidcap.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-vidout.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-overlay.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-vbi.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-selection.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-misc.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-streaming.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-sdr.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-edid.cpp',
				'v4l-utils_src/utils/v4l2-ctl/v4l2-ctl-modes.cpp',
				'v4l-utils_src/utils/v4l2-ctl/vivid-tpg-colors.c',
				'v4l-utils_src/utils/v4l2-ctl/vivid-tpg.c',
				
			],
			
			
		}
	
		
	]
}