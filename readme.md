# v4l-utils/v4l2 GYP Module

** Experimental **

expose v4l-utils/v4l2 through gyp

- can be used stand alone to compile v4l-utils as static/shared libraries 
	static/shared library can be changed in the variables section of v4l-utils.gyp
- can be used as part of a bigger gyp project (which was the original intent) :

```
'dependencies':[
	'v4l-utils.module/v4l-utils.gyp:v4l2'
]
```

v4l-utils git://linuxtv.org/v4l-utils.git


```
gyp v4l-utils.gyp -DOS=linux -Dtarget_arch=ia32 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux32/

gyp v4l-utils.gyp -DOS=linux -Dtarget_arch=x64 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux64/

gyp v4l-utils.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/
```

dependencies:

>libjpeg-turbo.module

>libglob (android ndk only)

