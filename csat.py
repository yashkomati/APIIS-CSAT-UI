import requests
import zipfile
import io
import os
import pandas as pd
import datetime
import time
import threading

def get_qualtrics_survey_data(dir_save_survey, survey_id):# dir_save_survey is the directory to which these exported files are to be saved.
   
    # Setting user Parameters
    api_token = "nEOlIxeWbcgAkcAbtk9uD8ZyT0YnCQV9AIIRQCcL"
    file_format = "csv"
    data_center = 'amazoneu.syd1' # "<Organization ID>.<Datacenter ID>"
    # Setting static parameters
    request_check_progress = 0
    progress_status = "in progress"
    base_url = "https://{0}.qualtrics.com/API/v3/responseexports/".format(data_center)
    headers = {
        "content-type": "application/json",
        "x-api-token": api_token,
    }
    # Step 1: Creating Data Export
    download_request_url = base_url
    download_request_payload = '{"format":"csv","useLabels": true ,"surveyId":"' + survey_id + '"}' # you can set useLabels:True to get responses in text format
    download_request_response = requests.request("POST", download_request_url, data=download_request_payload, headers=headers)
    progress_id = download_request_response.json()["result"]["id"]
    # print(download_request_response.text)
    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status != "complete":
        request_check_url = base_url + progress_id
        request_check_response = requests.request("GET", request_check_url, headers=headers)
        request_check_progress = request_check_response.json()["result"]["percentComplete"]
    # Step 3: Downloading file
    request_download_url = base_url + progress_id + '/file'
    request_download = requests.request("GET", request_download_url, headers=headers, stream=True)
    # Step 4: Unzipping the file
    zipfile.ZipFile(io.BytesIO(request_download.content)).extractall(dir_save_survey)
    print('Downloaded qualtrics survey')
path = "C:\\Users\\komatiyk\\Downloads\\Qualtrics Weekly Files"

# definining the suvery ID's with Specalist Names
Gurramr = "SV_0Ai7eAuueB6M6gJ"
ddlc = "SV_26alR8n753kAbyu"
dhahiman = "SV_8qdBdGLpsZRHAjA"
Fbhagat = "SV_9mn7lVJCPPAXNTn"
keziaidi = "SV_afMqjeuQ0UOg1qS"
khandh = "SV_8AmcjQKwidXNGG9"
komatiyk = "SV_eRHKjxVDveyIPoG"
mohlipsa = "SV_8w5mrVpJpX5RB6m"
parniv = "SV_6JqeQjoUW0D6RmK"
pratvel = "SV_9nSSDCPpLdaykf4"
Premalatha = "SV_29mXA0vS5qh5HqC"
prkujh= "SV_4HoXXHRb9ptxWbc"
prsrivas= "SV_42bdrRgDB7KUAiW"
rajchat= "SV_7ai49aIbpdjClnw"
tatii = "SV_efHw2haEtbUs7yK"
tgganesa = "SV_5bh19yBpdd1MF3o"
list = [ddlc, dhahiman, Fbhagat, keziaidi, komatiyk, mohlipsa, parniv, pratvel, Premalatha, prkujh, prsrivas, rajchat,tatii,tgganesa]
[get_qualtrics_survey_data(dir_save_survey = path, survey_id = i) for i in list]

ddlc = pd.read_csv("Technical Onboarding CSAT- 2022(ddlc).csv")
dhahiman = pd.read_csv("Technical Onboarding CSAT- 2022(dhahiman).csv")
Fbhagat = pd.read_csv("Technical Onboarding CSAT- 2022(Fbhagat).csv")
keziaidi = pd.read_csv("Technical Onboarding CSAT- 2022(keziaidi).csv")
komatiyk = pd.read_csv("Technical Onboarding CSAT- 2022(komatiyk).csv")
mohlipsa = pd.read_csv("Technical Onboarding CSAT- 2022(mohlipsa).csv")
parniv = pd.read_csv("Technical Onboarding CSAT- 2022(parniv).csv")
pratvel = pd.read_csv("Technical Onboarding CSAT- 2022(pratvel).csv")
Premalatha = pd.read_csv("Technical Onboarding CSAT- 2022(Premalatha).csv")
prkujh = pd.read_csv("Technical Onboarding CSAT- 2022(prkujh).csv")
rajchat = pd.read_csv("Technical Onboarding CSAT- 2022(rajchat).csv")
tgganesa = pd.read_csv("Technical Onboarding CSAT- 2022(tgganesa).csv")
tatii = pd.read_csv("Technical Onboarding CSAT- 2022(tatii).csv")

#List1 = (
#     Fbhagat = pd.read_csv("Technical Onboarding CSAT- 2022(Fbhagat).csv"),Premalatha = pd.read_csv("Technical Onboarding CSAT- 2022(Premalatha).csv"),ddlc = pd.read_csv("Technical Onboarding CSAT- 2022(ddlc).csv"),dhahiman = pd.read_csv("Technical Onboarding CSAT- 2022(dhahiman).csv"),keziaidi = pd.read_csv("Technical Onboarding CSAT- 2022(keziaidi).csv"),komatiyk = pd.read_csv("Technical Onboarding CSAT- 2022(komatiyk).csv"),mohlipsa = pd.read_csv("Technical Onboarding CSAT- 2022(mohlipsa).csv"),parniv = pd.read_csv("Technical Onboarding CSAT- 2022(parniv).csv"),pratvel = pd.read_csv("Technical Onboarding CSAT- 2022(pratvel).csv"),prkujh = pd.read_csv("Technical Onboarding CSAT- 2022(prkujh).csv"),
#     rajchat = pd.read_csv("Technical Onboarding CSAT- 2022(rajchat).csv"),tatii = pd.read_csv("Technical Onboarding CSAT- 2022(tatii).csv"),tgganesa = pd.read_csv("Technical Onboarding CSAT- 2022(tgganesa).csv")
# )

# # Names defined as in Astro Report: 'Harish Ganesan', 'Lakshmi Pratyusha Velamakanni', 'Farah Bhagat',
#        'Niveditha Parvatha', 'PRAKASH JHA', 'Premalatha maddirala',
#        'Himanshu Dhami', 'Yashwant Komati', 'Dilip Chavali',
#        'Indra Tatikonda', 'Rajarshi Chatterjee', 'Lipsa Mohanty',
#        'KEZIA IDIKKULA MUTHALALY'

## By doing the below we are adding a column SPOC with the Specalist's name against the feedback received and removing the extra header rows on individual file.

ddlc['SPOC'] = "DILIP CHAVALI"
ddlc.drop([0,1],inplace= True)
Fbhagat['SPOC'] = "FARAH BHAGAT"
Fbhagat.drop([0,1],inplace= True)
dhahiman['SPOC'] = "HIMANSHU DHAMI"
dhahiman.drop([0,1],inplace= True)
keziaidi['SPOC'] = "KEZIA IDIKKULA MUTHALALY"
keziaidi.drop([0,1],inplace= True)
komatiyk['SPOC'] = "YASHWANT KOMATI"
komatiyk.drop([0,1],inplace= True)
mohlipsa['SPOC'] = "LIPSA MOHANTY"
mohlipsa.drop([0,1],inplace= True)
parniv['SPOC'] = "NIVEDITHA PARVATHA"
parniv.drop([0,1],inplace= True)
pratvel['SPOC'] = "LAKSHMI PRATYUSHA VELAMAKANNI"
pratvel.drop([0,1],inplace= True)
Premalatha['SPOC'] = "PREMALATHA MADDIRALA"
Premalatha.drop([0,1],inplace= True)
prkujh['SPOC'] = "PRAKASH JHA"
prkujh.drop([0,1],inplace= True)
rajchat['SPOC'] = "RAJARSHI CHATTERJEE"
rajchat.drop([0,1],inplace= True)
tgganesa['SPOC'] = "HARISH GANESAN"
tgganesa.drop([0,1],inplace= True)
tatii['SPOC'] = "INDRA TATIKONDA"
tatii.drop([0,1],inplace= True)

df_merged = pd.concat([ddlc,dhahiman, Fbhagat, keziaidi, komatiyk, mohlipsa, parniv, pratvel, Premalatha, prkujh, rajchat, tgganesa, tatii])

df_merged # All Feedbacks

#Dropping unneccesary columns and renaming certain columns for easy reference.

merged_mod = df_merged.drop(columns=['ResponseID','ResponseSet','IPAddress','Score-sum','Score-weightedAvg','Score-weightedStdDev'])

merged_mod.rename(columns={'StartDate': 'Start_Date', 'EndDate': 'End_date','RecipientLastName': 'Specalist_Name', 'Q1': 'Rating of the overall Support','Q2_1': 'Knowledge of SP-API products & Services','Q2_2': 'Ability to communicate clearly','Q3': 'Merchant_Token', 'Q4': 'Comments'}, inplace=True)

merged_mod[['Start_Date','End_date']]= merged_mod[['Start_Date','End_date']].apply(pd.to_datetime)

merged_mod['Merchant_Token'].fillna('0')

merged_mod

merged_mod['Key'] = merged_mod.Merchant_Token.str.cat(merged_mod.SPOC)

merged_mod.to_csv('Merged_FB_File.csv') # Converting the aggregated feedbacks to a CSV file

#Final Feedback file

astro = pd.read_csv('DataAstro.csv') # Importing astro report

# Creating a column "Key" which is a combination of Merchant Token + the Speclalist's name, which would help us compare the feedbacks with cases on Astro
astro['owner'] = astro['owner'].str.upper()
astro['Key'] = astro.encrypt_id.str.cat(astro.owner)

#Converting the data type of Complete date and start date to Time Format, which is currently is a pandas series format.

# # astro['listing_complete_date'] = pd.to_datetime(astro['listing_complete_date'], format='%Y-%m-%d')
# # astro['create_date'] = pd.to_datetime(astro['create_date'], format='%Y-%m-%d')
astro['merchant_customer_id'].fillna(0)
astro[['run_date','integration_start_date','handoff_date','listing_complete_date','create_date']]= astro[['run_date','integration_start_date','handoff_date','listing_complete_date','create_date']].apply(pd.to_datetime)

astro.head()

# convert and downloads the CSV
#astro.to_csv('Astro_Merged') 

# Pivot table to show cases details against each individual

astro_pivot = pd.pivot_table(astro, index =['owner'], values=['case_number'], columns=['status'], aggfunc= 'count', fill_value = 0)

astro_pivot.to_csv('astro_pivot.csv')


# gives all 2022 cases with all the statuses
astro_all_22 = astro.loc[(astro['create_date'] >= '2022-01-01')]

#(astro.loc[(astro['listing_complete_date'] >= '2022-01-01') & (astro['listing_complete_date'] < '2022-12-31')]) 

astro_all_22.to_csv('astro_all_22.csv')

astro_all_22.head(3)

astro_completed= astro[astro['status'] =='Completed']

# astro_completed.head(3)

astro_completed_22 = (astro_completed.loc[(astro_completed['listing_complete_date'].between('2022-01-01','2022-12-31'))])

#astro_completed_22 = (astro_completed.loc[(astro_completed['listing_complete_date'] >= '2022-01-01') & (astro_completed['listing_complete_date'] < '2022-12-31')])

astro_completed_22.to_csv('astro_completed_22.csv')

astro_completed_22.head(3) # gives all 2022 cases that are completed

look_up = pd.merge(astro_completed_22,merged_mod[['Key',"SPOC"]], on = 'Key', how= 'left') # Merges and compares feedbacks

# compares owner = spoc, if yes, makes its Feedback 'Yes'. Else: 'No'
look_up.loc[look_up['owner']== look_up['SPOC'], 'Feedback_Received'] = 'Yes'

look_up.loc[look_up['owner']!= look_up['SPOC'], 'Feedback_Received'] = 'No'

look_up = look_up.drop_duplicates(subset=["case_number"], keep='last')

look_up.to_csv('look_up.csv')

#csat_pivot_df 


tmp_df = look_up[look_up['listing_complete_date'].notnull()]
tmp_df = tmp_df[['Feedback_Received', 'owner']].copy()
pivot_table = tmp_df.pivot_table(
    index=['owner'],
    columns=['Feedback_Received'],
    values=['Feedback_Received'],
    aggfunc={'Feedback_Received': ['count']}
)
pivot_table.columns = [ '_'.join([str(c) for c in c_list]) for c_list in pivot_table.columns.values ]

look_up_pivot = pivot_table.reset_index()

# Changed Feedback_Received count Yes to dtype int
look_up_pivot['Feedback_Received_count_Yes'] = look_up_pivot['Feedback_Received_count_Yes'].fillna(0).astype('int')

# Changed Feedback_Received count No to dtype int
look_up_pivot['Feedback_Received_count_No'] = look_up_pivot['Feedback_Received_count_No'].fillna(0).astype('int')

# # Reordered column Feedback_Received count Yes
look_up_pivot_columns = [col for col in look_up_pivot.columns if col != 'Feedback_Received_count_Yes']
look_up_pivot_columns.insert(1, 'Feedback_Received_count_Yes')
look_up_pivot = look_up_pivot[look_up_pivot_columns]

# # Renamed columns APIIS_Specalist
look_up_pivot.rename(columns={'owner': 'APIIS_Specalist'}, inplace=True)

# # Renamed columns Feedback_Received (Yes)
look_up_pivot.rename(columns={'Feedback_Received_count_Yes': 'Feedback_Received (Yes)'}, inplace=True)

# # Renamed columns Feedback_Received (No)
look_up_pivot.rename(columns={'Feedback_Received_count_No': 'Feedback_Received (No)'}, inplace=True)

# # Added column new-column-fspg
look_up_pivot.insert(3, 'Total Completed Cases', 0)

# # Set formula of Total Completed Cases
look_up_pivot['Total Completed Cases'] = look_up_pivot['Feedback_Received (Yes)']+look_up_pivot['Feedback_Received (No)']

# # Added column new-column-ucte
look_up_pivot.insert(4, 'CSAT Response Rate (%)', 0)

# # Set formula of CSAT Response Rate (%)
look_up_pivot['CSAT Response Rate (%)'] = (look_up_pivot['Feedback_Received (Yes)']/look_up_pivot['Total Completed Cases']) * 100

# # Formatted dataframes. View these styling objects to see the formatted dataframe
look_up_pivot_styler = look_up_pivot.style\
.format("{:,.2%}", subset=['CSAT Response Rate (%)'])
   
look_up_pivot

look_up_pivot.to_csv('CSAT_RR_Pivot.csv')

# Individual Case Level Metrics:

tmp_df_1 = astro_all_22[['owner', 'status']].copy()
pivot_table = tmp_df_1.pivot_table(
    index=['owner'],
    columns=['status'],
    values=['status'],
    aggfunc={'status': ['count']}
)
pivot_table.columns = [ '_'.join([str(c) for c in c_list]) for c_list in pivot_table.columns.values ]
astro_all_22_pivot = pivot_table.reset_index()

# Changed status count Awaiting Information to dtype int
astro_all_22_pivot['status_count_Awaiting Information'] = astro_all_22_pivot['status_count_Awaiting Information'].fillna(0).astype('int')

# # Changed status count Cancelled to dtype int
astro_all_22_pivot['status_count_Cancelled'] = astro_all_22_pivot['status_count_Cancelled'].fillna(0).astype('int')

# # Changed status count Completed to dtype int
astro_all_22_pivot['status_count_Completed'] = astro_all_22_pivot['status_count_Completed'].fillna(0).astype('int')

# # Changed status count Submitted to dtype int
astro_all_22_pivot['status_count_Submitted'] = astro_all_22_pivot['status_count_Submitted'].fillna(0).astype('int')

# # Changed status count WIP to dtype int
astro_all_22_pivot['status_count_WIP'] = astro_all_22_pivot['status_count_WIP'].fillna(0).astype('int')

# # Renamed columns APIIS_Specalist
astro_all_22_pivot.rename(columns={'owner': 'APIIS_Specalist'}, inplace=True)

# # Renamed columns Awatiting Information
astro_all_22_pivot.rename(columns={'status_count_Awaiting Information': 'Awaiting_Information'}, inplace=True)

# # Renamed columns Cancelled
astro_all_22_pivot.rename(columns={'status_count_Cancelled': 'Cancelled'}, inplace=True)

# # Renamed columns Completed
astro_all_22_pivot.rename(columns={'status_count_Completed': 'Completed'}, inplace=True)

# # Renamed columns Submitted
astro_all_22_pivot.rename(columns={'status_count_Submitted': 'Submitted'}, inplace=True)

# # Renamed columns WIP
astro_all_22_pivot.rename(columns={'status_count_WIP': 'WIP'}, inplace=True)

# # Reordered column Submitted
astro_all_22_pivot_columns = [col for col in astro_all_22_pivot.columns if col != 'Submitted']
astro_all_22_pivot_columns.insert(1, 'Submitted')
astro_all_22_pivot = astro_all_22_pivot[astro_all_22_pivot_columns]

# # Reordered column WIP
astro_all_22_pivot_columns = [col for col in astro_all_22_pivot.columns if col != 'WIP']
astro_all_22_pivot_columns.insert(3, 'WIP')
astro_all_22_pivot = astro_all_22_pivot[astro_all_22_pivot_columns]

astro_all_22_pivot.insert(6, 'Total Cases', 0)

astro_all_22_pivot['Total Cases'] = astro_all_22_pivot['Submitted'] + astro_all_22_pivot['Awaiting_Information']+ astro_all_22_pivot['WIP'] + astro_all_22_pivot['Cancelled'] + astro_all_22_pivot['Completed']
#astro_all_22_pivot[] = sum(astro_all_22_pivot['Submitted'],astro_all_22_pivot['Awaiting_Information'],astro_all_22_pivot['WIP'],astro_all_22_pivot['Cancelled'],astro_all_22_pivot['Completed'])

astro_all_22_pivot

astro_all_22_pivot.to_csv('Case_Level_Metrics_Pivot.csv')
