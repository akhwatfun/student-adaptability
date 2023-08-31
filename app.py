import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image


st.set_page_config(page_title="Students Adaptability Level in Online Education", layout="wide")


def user_input_features():
    st.sidebar.header('Input Manual')
    gender = st.sidebar.selectbox('Gender', ['Boy', 'Girl'])
    age = st.sidebar.selectbox('Age', ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30'])
    education_level = st.sidebar.selectbox('Education Level', ['School', 'College', 'University'])
    institution_type = st.sidebar.selectbox('Institution Type', ['Government', 'Non Government'])
    it_student = st.sidebar.selectbox('IT Student', ['No', 'Yes'])
    location_in_town = st.sidebar.selectbox('Location in Town', ['Yes', 'No'])
    load_shedding = st.sidebar.selectbox('Load-shedding', ['Low', 'High'])
    financial_condition = st.sidebar.selectbox('Financial Condition', ['Poor', 'Mid', 'Rich'])
    internet_type = st.sidebar.selectbox('Internet Type', ['Wifi', 'Mobile Data'])
    network_type = st.sidebar.selectbox('Network Type', ['2G', '3G', '4G'])
    class_duration = st.sidebar.selectbox('Class Duration', ['0', '1-3', '3-6'])
    self_lms = st.sidebar.selectbox('Self LMS', ['No', 'Yes'])
    device = st.sidebar.selectbox('Device', ['Tab', 'Mobile', 'Computer'])

    # Create input dictionary with label-to-numeric mapping
    label_to_numeric = {
        'Boy': 1,
        'Girl': 0,
        '1-5': 0,
        '6-10': 1,
        '11-15': 2,
        '16-20': 3,
        '21-25': 4,
        '26-30': 5,
        'School': 0,
        'College': 1,
        'University': 2,
        'Government': 1,
        'Non Government': 0,
        'No': 0,
        'Yes': 1,
        'Yes': 1,
        'No': 0,
        'Low': 0,
        'High': 1,
        'Poor': 1,
        'Mid': 2,
        'Rich': 3,
        'Wifi': 2,
        'Mobile Data': 1,
        '2G': 1,
        '3G': 2,
        '4G': 3,
        '0': 0,
        '1-3': 1,
        '3-6': 2,
        'No': 0,
        'Yes': 1,
        'Tab': 1,
        'Mobile': 2,
        'Computer': 3
    }

    # Create input dictionary
    data = {
            'Gender': label_to_numeric[gender],
            'Age': label_to_numeric[age],
            'Education Level': label_to_numeric[education_level],
            'Institution Type': label_to_numeric[institution_type],
            'IT Student': label_to_numeric[it_student],
            'Location in Town': label_to_numeric[location_in_town],
            'Load-shedding': label_to_numeric[load_shedding],
            'Financial Condition': label_to_numeric[financial_condition],
            'Internet Type': label_to_numeric[internet_type],
            'Network Type': label_to_numeric[network_type],
            'Class Duration': label_to_numeric[class_duration],
            'Self LMS': label_to_numeric[self_lms],
            'Device': label_to_numeric[device]
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

def run():
    st.write("""
    # Adaptability Prediction in Online Education Dashboard
    This dashboard created by : [@fitrirachmawati](https://www.linkedin.com/in/fitrirachmawati1004/)
    
    This app is to predict the level of student adaptability in online education. 
    This application can assist users (in this case, educators or educational administrators) 
    in predicting to what extent a student can adapt to the online learning environment based on various input features or factors.
    """)

    # Sidebar inputs
    st.sidebar.header('Input Features')
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is None:
        input_df = user_input_features()
    else:
        input_df = pd.read_csv(uploaded_file)

    # Display user's selected inputs
    st.image("online-school.png", width=500)
    # Define dictionaries for mapping numerical values to strings
    gender_dict = {1: 'Boy', 0: 'Girl'}
    age_dict = {0: '1-5', 1: '6-10', 2: '11-15', 3: '16-20', 4: '21-25', 5: '26-30'}
    education_level_dict = {0: 'School', 1: 'College', 2: 'University'}
    institution_type_dict = {1: 'Government', 0: 'Non Government'}
    it_student_dict = {0: 'No', 1: 'Yes'}
    location_in_town_dict = {1: 'Yes', 0: 'No'}
    load_shedding_dict = {0: 'Low', 1: 'High'}
    financial_condition_dict = {1: 'Poor', 2: 'Mid', 3: 'Rich'}
    internet_type_dict = {2: 'Wifi', 1: 'Mobile Data'}
    network_type_dict = {1: '2G', 2: '3G', 3: '4G'}
    class_duration_dict = {0: '0', 1: '1-3', 2: '3-6'}
    self_lms_dict = {0: 'No', 1: 'Yes'}
    device_dict = {1: 'Tab', 2: 'Mobile', 3: 'Computer'}

    # Display user inputs in string format
    st.write('User Inputs:')
    input_data = {
        'Feature': ['Gender', 'Age', 'Education Level', 'Institution Type', 'IT Student',
                    'Location in Town', 'Load-shedding', 'Financial Condition', 'Internet Type',
                    'Network Type', 'Class Duration', 'Self LMS', 'Device'],
        'Value': [gender_dict[input_df['Gender'].values[0]],
                age_dict[input_df['Age'].values[0]],
                education_level_dict[input_df['Education Level'].values[0]],
                institution_type_dict[input_df['Institution Type'].values[0]],
                it_student_dict[input_df['IT Student'].values[0]],
                location_in_town_dict[input_df['Location in Town'].values[0]],
                load_shedding_dict[input_df['Load-shedding'].values[0]],
                financial_condition_dict[input_df['Financial Condition'].values[0]],
                internet_type_dict[input_df['Internet Type'].values[0]],
                network_type_dict[input_df['Network Type'].values[0]],
                class_duration_dict[input_df['Class Duration'].values[0]],
                self_lms_dict[input_df['Self LMS'].values[0]],
                device_dict[input_df['Device'].values[0]]]
    }

    input_df_display = pd.DataFrame(input_data)
    input_df_display.index = [''] * len(input_df_display)  # Clear the index column
    st.table(input_df_display)

    #st.write('User Inputs:')
    #st.dataframe(input_df.style.set_properties(**{'text-align': 'left'}))
    if st.sidebar.button('Predict!'):
        df = input_df
        st.write(df)
        loaded_model = pickle.load(open('best_model_logreg_new.pkl', 'rb'))
        prediction = loaded_model.predict(df)  
        result = ['Cannot Adaptive' if prediction == 0 else 'Yes Can Adaptive']
        st.subheader('Prediction: ')
        output = str(result[0])
        with st.spinner('Wait for it...'):
            time.sleep(4)
            st.success(f"Prediction of this app is {output}")

if __name__ == "__main__" :
   run()
