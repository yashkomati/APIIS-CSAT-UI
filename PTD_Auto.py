import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
# from streamlit_option_menu import option_menu
#import lxml

st.set_page_config(layout="wide", page_icon=":Amazon:", page_title="Amazon XML/JSON Generator")

# with st.sidebar:
	# menu = option_menu(menu_title = "Navigation", options = ["Home","Search",'Contact'],icons =["house","search","send"], orientation='horizontal', default_index= 0, menu_icon= 'cast')


Camcorder_xsd = """<?xml version="1.0" encoding="UTF-8"?>
<AmazonEnvelope xsi:noNamespaceSchemaLocation="amzn-envelope.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Header>
		<DocumentVersion>1.01</DocumentVersion>
		<MerchantIdentifier>A1FQ5TD7QOKRTO</MerchantIdentifier>
	</Header>
	<MessageType>Product</MessageType>
	<Message>
		<MessageID>1</MessageID>
		<OperationType>Update</OperationType>
		<Product>
			<SKU>B08NPYXT4B</SKU>
			<StandardProductID>
				<Type>ASIN</Type>
				<Value>B08NPYXT4B</Value>
			</StandardProductID>
			<Condition>
				<ConditionType>New</ConditionType>
			</Condition>
			<DescriptionData>
				<Title>AKASO Brave 7 Action Camera, IPX8 Waterproof Native 4K 20MP WiFi Cam with Touch Screen EIS 2.0 Zoom Support External Mic Voice Control Vlog Camera</Title>
                        <Brand>AKASO</Brand>
				<Description>4K30FPS Video/ 20MP Photo/ IPX8 10M/33FT Waterproof Camera without case/ Visual Remote Control/</Description> 
				<BulletPoint>Upgrade series of AKASO Brave 7 LE: Featuring 4K30fps, 2.7K30FPS video resolution and 20MP</BulletPoint> 
				<BulletPoint>10M/33FT Waterproof Camera without Cas</BulletPoint>
				<ItemDimensions>
          <Length unitOfMeasure="CM">35</Length>
          <Width unitOfMeasure="CM">15</Width>
          <Height unitOfMeasure="CM">21</Height>
          <Weight unitOfMeasure="GR">702.50</Weight>
        </ItemDimensions>
        <PackageDimensions>
          <Length unitOfMeasure="CM">35</Length>
          <Width unitOfMeasure="CM">15</Width>
          <Height unitOfMeasure="CM">21</Height>
          <Weight unitOfMeasure="GR">702.50</Weight>
        </PackageDimensions>
        <MaxOrderQuantity>5</MaxOrderQuantity>

				<Manufacturer>AKASO</Manufacturer> 
				<MfrPartNumber>AKASO Brave 7</MfrPartNumber>
				<SearchTerms>Storage</SearchTerms> 
				<RecommendedBrowseNode>3077037031</RecommendedBrowseNode>
				<CountryOfOrigin>uk</CountryOfOrigin>
				<UnitCount>1</UnitCount>
        <PPUCountType>count</PPUCountType>
 <IsExpirationDatedProduct>false</IsExpirationDatedProduct>
			</DescriptionData>
			<ProductData>
				<CE>
					<ProductType>
						<CECamcorder>
						</CECamcorder>
					</ProductType>
				</CE>
			</ProductData>
		</Product>
</Message>
<Message>"""

#title of the page:

st.title('Amazon XML Generator for SP-API')

st.header('This app allows you to generate and download the XML or JSON files for your respective product type.')

primary_category = st.selectbox(label="Please pick your primary category",options=['Consumer Electronics', 'Home', 'Jewellery', 'Other'])

if primary_category == 'Consumer Electronics':
    product_type =st.selectbox('Please select your ProductType', options=['CECamcorder','Mobile Phones','Accessories','Smart Watches', 'Other'])
    if product_type == 'CECamcorder':
        st.markdown("**Please find the sample XML for your product type:**" +" "+ product_type +" "+"**below:**" )
		# textblock_col, down_button = st.columns(2)
        st.markdown("*You could either copy the code from the code block below or download it as .txt file*")
		# down_button.button("Download the XSD as a Text File")
        st.code(Camcorder_xsd, language="XSD")
	# else:
	# 	st.write('Your selected product_type is not available yet, please check back soon!')
else:
	st.write(" Please standby we are adding more categories")

st.header(":mailbox: Please share your feedback or request with us!")

contact_form = """
<form action="https://formsubmit.co/komatiyk@amazon.com" method="POST">
	 <input type="hidden" name="_captcha" value="false">
	 <input type="hidden" name="_cc" value="parniv@amazon.com">
	 <input type="hidden" name="_autoresponse" value="We've received your message and will be sure to get back to you with an update soon!">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
	 <textarea name= "message" placeholder = "Please let us know your feedback or a request, if any"></textarea>
     <button type="submit">Send</button>
</form> 
"""

st.markdown(contact_form, unsafe_allow_html=True)

# code to use the local CSS File

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("PTDstyle.css.txt")