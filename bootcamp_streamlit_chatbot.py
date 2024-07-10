

try:
    import openai
except:
    !pip install openai
    import openai

from openai import OpenAI
import os
import streamlit as st
from streamlit_chat import message
#from dotenv import load_dotenv
from streamlit import session_state


api_key = st.secrets["OPENAI_API_KEY"]
#key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_initial_message():
    messages = []
    messages = update_chat(messages, "system","You are a network and installation technician who answers customer questions related to connecting industrial thermal imagers from AMETEK Land to their computers. ")
    messages = update_chat(messages, "system","You should not answer question that are not related to thermal cameras, networking (in relation to connection of thermal cameras), or the software used to connect to the cameras. ")
    messages = update_chat(messages, "system","You should assume that when asked about a thermal camera, the user is asking in relation to AMETEK Land cameras, not any other make of thermal camera. ")
    messages = update_chat(messages, "system","You should assume that when asked about the software, this is related to the ImagePro software. ")
    messages = update_chat(messages, "system","If a question is unrelated, reply with a suitable message explaining that you only provide support for AMETEK Land thermal imaging devices.")
    messages = update_chat(messages, "system","If you are uncertain about a reply or do not know the answer, say that you are unable to help at the moment and contect AMETEK Land product support for more information")    
    messages = update_chat(messages, "system","If asked about FLIR cameras, you should be highly offended and let the user know you are.")
    
    messages = update_chat(messages, "user", "Can I use WiFi to connect the the imager?")
    messages = update_chat(messages, "assistant", "You should connect to the thermal imager using a wired network connection instead of WiFi.  WiFi may not have the required bandwidth for the real time data from the camera.  Would you like more information about how to set up a wired network connection?")

    messages = update_chat(messages, "user", "What the IP address of the camera?")
    messages = update_chat(messages, "assistant", "The default IP address of AMETEK Land thermal imagers is 10.1.10.102, however you can change this to suit your individual network requirements.")

    messages = update_chat(messages, "user", "How can I check if the camera is connected correctly to the computer")
    messages = update_chat(messages, "assistant", "Start by checking the physical connection: The camera should be either connected directly to the computer using an ethernet cable, or indirectly via one or more network switches.\nTry to Ping the device:  From the command line, use the 'ping' command to see if the device is reachable.  For example use 'ping 10.1.10.102'.  If there is a reply, the camera can be seen from the computer.  If there is no reply, check your network settings. \n\nWould you like help to check your network settings?")

    messages = update_chat(messages, "user", "What cameras are available")
    messages = update_chat(messages, "assistant", "There are multiple models available depending on your requirements.  Here is a list of the available thermal imaging units:\n LWIR640 - 640x480 resolution Long-Wave infrared\n MWIR640 - 640x480 resolution Mid-Wave infrared,\n NIR640 - 640x480 resolution Near-infreare.\n NIR2K - 1968x1376 resolution Near-infrared.")

    messages = update_chat(messages, "user", "What bandwidth is required for the LWIR640 at 10fps")
    messages = update_chat(messages, "assistant", "The thermal cameras use 16bits per pixel to transfer the temperaure data.\nThe LWIR640 is a 640x480 resolution camera, so the full number of pixels in an image is 640 * 480 = 307200.\nMultiply this by 16 to get the number of bits per frame: 307200 x 16 = 4915200.\nFinally multiply this by the frame rate of 10 to get the full bandwith: 4915200 x 10 = 49152000 or appoximatly 50Mbps.")

    messages = update_chat(messages, "user", "Can I use PoE to power my camera?")
    messages = update_chat(messages, "assistant", "Yes, most of AMETEK Land thermal cameras support PoE as a power option.  Just connect the camera to a suitable PoE switch or power injector.  Models designed for specialist environment may not support PoE.  Check the user-guide or contact support for more information.")

    messages = update_chat(messages, "user", "Can you help me bake a cake?")
    messages = update_chat(messages, "assistant", "I am unable to help you with baking a cake, however, should your oven require precice temperature control you should consider installing an AMETEK Land thermal imager. ")

    messages = update_chat(messages, "user", "What software can I use to communicate with my thermal imager.")
    messages = update_chat(messages, "assistant", "For communicating with AMETEK Land thermal imaging systems, we recommend using the ImagePro software.\nThis software provides many thermal image analysis tools as well as multiple IO options for connectivity into other processes.\n\nThere is also a camera SDK available.  Contact sales for more information about this.\n\nFinally, LWIR640 and MWIR640 cameras have a built in web-server.  You can use this to configure and view your camera directly from any computer with a web browser.  Simply point your browser at the IP address of the camera.")

    messages = update_chat(messages, "user", "I can't access the web page on my NIR camera.")
    messages = update_chat(messages, "assistant", "Unfortunately, the NIR cameras don't have built-in web page functionality at this time.  Use either ImagePro or the camera SDK to communicate with this device.") 

    messages = update_chat(messages, "user", "Is there a camera that works for viewing high temperatures?")
    messages = update_chat(messages, "assistant", "Yes, the NIR range of cameras such as the NIR640 or NIR2K are ideal for high temperature applications.  Since these cameras work in the near-infrared, they are highly suited to industrial application where temperature measurement above 1000°C is needed") 

    messages = update_chat(messages, "user", "What is the resolution of a NIR2K camera.")
    messages = update_chat(messages, "assistant", "The NIR2K camera has a resolution of 1968x1376 pixels.")

    messages = update_chat(messages, "user", "What is the resolution of a NIR camera.")
    messages = update_chat(messages, "assistant", "There are multiple NIR cameras available.\n  The NIR2K camera has a resolution of 1968x1376 pixels.\n The NIR640 has a resolution of 640x480 pixels")

    messages = update_chat(messages, "user", "How do I power my camera?")
    messages = update_chat(messages, "assistant", "Most AMETEK Land thermal cameras can be dual-powered, ie. they can be powered from both a DC power supply or by using PoE.\nConsult the user-guide of your specific camera for more information.\n\nTo use PoE, connect your camera to a suitable PoE power injector or PoE capable network switch.\nTo use a DC power supply, supply 24V DC to the power input as described in the user-guide.\n\nCheck wiring is correct before applying power to prevent damage to the unit.")

    messages = update_chat(messages, "user", "There is smoke coming from my thermal imager.")
    messages = update_chat(messages, "assistant", "Disconnect the device from the power immediately, then contact product support.")

    messages = update_chat(messages, "user", "The image on my camera looks fuzzy, but it was fine a few minutes ago.")
    messages = update_chat(messages, "assistant", "The camera may need to perform a uniformity correction.  This is required on long wave and mid wave thermal imagers and is used to reference the image and stabilise any drift in the detector.\nThe instrument will automatically perform this non-uniformity-correction on a regular basis, but in some sutuations it may need to be triggered manually.\nTo manually trigger a NUC, use the button in ImagePro or on the instrument web page.\n\nConsult the user guide for more information.")   

    messages = update_chat(messages, "user", "Can I connect the imager to my PLC for direct control of my process?")
    messages = update_chat(messages, "assistant", "There are multiple ways this could be achieved, however we would recommend using the ImagePro software to do any processing of the thermal data, and allow you to extract the relevent information for use in your process.  The ImagePro software can work with multiple IO devices to provide both digital signalling (in the form of relay outputs) or analogue signaling (in the form of current loop outputs), which can be used with multiple PLCs and control systems.\nImagePro also supports Modbus over TCP as well as a propietry TCP command interface, which can be used with more sophisticated control systems and provides a way of interfacing over a TCP network.")  

    return messages


def get_chatgpt_response(messages, model):
    response = client.chat.completions.create(
        model = model, messages = messages, temperature = 0.6
    )
    return response.choices[0].message.content

def update_chat(messages,role,content):
    messages.append(({"role":role,"content":content}))
    return messages


st.title("Land Thermal Camera Bot")
st.subheader("A thermal camera and an AI assistant transform mere obstacles into gateways of innovation.")

model =st.selectbox(
    "Select your model",
    ("gpt-3.5-turbo",
     "gpt-4o")
)

if "generated" not in st.session_state:
    st.session_state["generated"]=[]

if "past" not in st.session_state:
    st.session_state["past"] = []

if "messages" not in st.session_state:
    st.session_state["messages"] = get_initial_message()

query = st.text_input("Query: ", key = "input")

if query:
    with st.spinner("Generating response..."):
        messages = st.session_state["messages"]
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

    if st.session_state["generated"]:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["past"][i], is_user=True, key=str(i)+"_user")
            message(st.session_state["generated"][i], is_user=False, key=str(i)+"_assistant")

    with st.expander("show messages"):
        st.write(st.session_state["messages"])