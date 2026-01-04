[app]
# (str) Title of your application
title = Drift Commander

# (str) Package name
package.name = driftcommander

# (str) Package domain (needed for android packaging)
package.domain = org.nothing.drift

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (Included kv and png)
source.include_exts = py,png,jpg,kv,ttf

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Added pygame and pyserial for your PS5 controller and Bluetooth
requirements = python3,kivy,pygame,pyserial

# (str) Icon of the application
# --- THIS IS THE KEY CHANGE FOR YOUR icon.png ---
icon.filename = icon.png

# (str) Supported orientations
orientation = portrait

# (list) Permissions 
# Needed for your Nothing Phone to talk to the HC-05
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, ACCESS_FINE_LOCATION

# (int) Android API to use (33 is good for Nothing Phone 3a)
android.api = 33

# (int) Minimum API your app will support
android.minapi = 21

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) indicates if the application should be full screen
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1