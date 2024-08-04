# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org/>

# Written by Nima Zeighami
# at the Brilliant Frame Launch Hackathon on August 3rd, 2024

import asyncio
from frame_sdk import Frame
from frame_sdk.camera import Quality, AutofocusType
from frame_sdk.display import Alignment, PaletteColors

async def main():
    # the with statement handles the connection and disconnection to Frame
    async with Frame() as frame:

        # Prints "Connected to Frame" in your CLI, not on the Frame
        print("Connected to Frame")

        # Prints current battery percentage in your CLI, not on the Frame
        print(f"Frame battery is {await frame.get_battery_level()}%")

        # Welcomes the user to NimaCam by printing text to Frame
        await frame.display.show_text("Welcome to NimaCam", align=Alignment.MIDDLE_CENTER)
        await frame.delay(3)

        # Prints text to Frame that communicates the purpose of the app
        await frame.display.show_text("This is a simple Camera app that captures a photo from your Frame to the directory it's being ran from", align=Alignment.MIDDLE_CENTER)
        await frame.delay(5)

        # Prints text to Frame that prompts the user to tap Frame to capture a photo
        await frame.display.show_text("Tap your Frame to take a photo", align=Alignment.MIDDLE_CENTER)
        await frame.motion.wait_for_tap()

        # Once user taps, prints text ot Frame that says "Capturing Photo" while Frame completes the image capture workflow
        await frame.run_lua("frame.display.text('Capturing Photo', 50, 100);frame.display.show()")

        # Frame captures a photo from the on-board camera and saves it to the directory NimaCam.py was run from
        photo_bytes = await frame.camera.take_photo(autofocus_seconds=2, quality=Quality.HIGH, autofocus_type=AutofocusType.CENTER_WEIGHTED)
        with open("NimaCam Photo.jpg", "wb") as file:
            file.write(photo_bytes)

        # Confirmation of image capture and call-to-action to tap to exit the app
        await frame.run_lua("frame.display.text('Photo captured - tap to exit', 50, 100);frame.display.show()")
        await frame.motion.wait_for_tap()

        # After user taps, this clears the Frame display
        await frame.display.show_text(" ", align=Alignment.MIDDLE_CENTER)

    # When program scope leaves the with statement, the connection is automatically closed

    # Prints "Disconnected from Frame" in your CLI, not on the Frame
    print("Disconnected from Frame")

# In general, make sure to run frame apps asynchronously
asyncio.run(main())