# NimaCam for Brilliant Frame

This is a simple camera app for the Brilliant Frame smartglasses written in Python. The app plays an intro describing itself, allows the user to tap to trigger a capture, and after capture is complete, prompts the user to tap to quit the app and clear the Frame's display.

This app was written very quickly alongside other demo apps at the Brilliant Frame Launch Hackathon across a total of, like, 5 hours. All the apps I wrote heavily borrow from the work already done to write sample code for the Brilliant Frame. You can find the documentation for Brilliant Frame here: https://docs.brilliant.xyz/frame/frame/

***

The only dependencies that are required for this app are Python3, pip3, and the Frame-SDK for Python.

If all dependencies are installed, you can run NimaCam.py from your CLI with the following command:

python3 NimaCam.py

From the directory NimaCam.py is in. NimaCam will automatically start a connection with your Frame glasses and begin to run. After you exit the app, you can find your captured image in the same directory you ran NimaCam.py from.

***

Brilliant Frame is an interesting product and developer platform. It was pretty easy to get going, connect over Bluetooth Low Energy (BLE) and draw to the screen. The fact that it's compatible with any Bluetooth device, including devices running Windows, MacOS, Linux, Android, and iOS is really compelling.

The SDK and APIs are not very mature yet, but they work, and getting started is easy.

To learn more about Brilliant Frame, go to the Brilliant Labs website: http://www.brilliant.xyz
