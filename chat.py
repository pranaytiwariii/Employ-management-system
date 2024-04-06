# Modules
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

#-----------------------------------------------------------------------------------------------------------------------------------
def main():

    st.set_page_config(page_title = "EMS") 
    
    #-----------------------------------------------------------------------------------------------------------------------------------
    # Create a SQLite database connection
    conn = sqlite3.connect('employee_data.db')
    c = conn.cursor()

    # Create Employee table
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT,
                    department TEXT,
                    position TEXT
                )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


    #-----------------------------------------------------------------------------------------------------------------------------------
    # Sidebar
        
    def show_contact():
        st.sidebar.write("---")
        st.sidebar.markdown("""<p style="color: #faca2b; font-weight: bold; font-size: 24px;">Contact</p>""", unsafe_allow_html=True)
        st.sidebar.markdown("""<p style="margin-bottom: 5px;">Made By : Shashank Singh</p>
        <p style="margin-bottom: 5px;">Version : 1.0</p>
        <p style="margin-bottom: 5px;">Connect with me :</p>
        <div style="display: flex; margin-bottom: 5px;">
            <a href="mailto:singhshashankthakur596@gmail.com" target="_blank" style="margin-right: 10px;">
                <img width="30" height="30" src="https://img.icons8.com/ios-filled/50/FAB005/gmail-new.png" alt="gmail-new"/>
            </a>
            <a href="https://www.linkedin.com/in/shashank-singh-230911249/" target="_blank" style="margin-right: 10px;">
                <img width="30" height="30" src="https://img.icons8.com/ios-filled/50/FAB005/linkedin.png" alt="linkedin"/>
            </a>
            <a href="https://github.com/ShashankSingh614" target="_blank" style="margin-right: 10px;">
                <img width="30" height="30" src="https://img.icons8.com/glyph-neue/64/FAB005/github.png" alt="github"/>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
    #-----------------------------------------------------------------------------------------------------------------------------------
    def EmployeeInformationManagement():
        st.header("Employee Information Management")
        st.write("---")
        st.write("Welcome to the Employee Information Management system, where every keystroke brings a new member to your team! Let's grow together!")
        
        def add_employee(name, email, phone, department, position):
            conn = sqlite3.connect('employee_data.db')
            c = conn.cursor()
            c.execute('''INSERT INTO employees (name, email, phone, department, position) VALUES (?, ?, ?, ?, ?)''', (name, email, phone, department, position))
            conn.commit()
            conn.close()
            st.success("Employee added successfully!")
        
        # Form to input employee details
        with st.form("employee_form"):
            name = st.text_input("Name",key="emp_name")
            email = st.text_input("Email",key="emp_email")
            phone = st.text_input("Phone",key="emp_phone")
            department = st.text_input("Department",key="emp_department")
            position = st.text_input("Position",key="emp_position")
            experience = st.text_input("Experience",key="emp_position")
            
            submit_button = st.form_submit_button("Add Employee")
        
        if submit_button:
            if name and email and phone and department and position:
                add_employee(name, email, phone, department, position)
            else:
                st.error("Please fill in all fields.")
    #-----------------------------------------------------------------------------------------------------------------------------------
    def AttendanceTracking():
        st.header("Attendance Tracking")
        st.write("---")
        
        #chatgpt
        # Store generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Hello there! I'm JAVIS, your friendly virtual assistant, at your service! Need assistance in tracking attendance records? No problem! Simply provide me with the details, and I'll ensure accurate monitoring and reporting of attendance for your team."}]
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt := st.chat_input("Say something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)     
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
                    pass
            st.session_state.messages.append(message)
            
    #-----------------------------------------------------------------------------------------------------------------------------------
    def LeaveManagement():
        st.header("Leave Management")
        st.write("---")
        
        #chatgpt
        # Store generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Hello there! I'm JAVIS, your friendly virtual assistant, at your service! Managing leave requests can be a breeze with my assistance! Whether it's submitting a request, checking leave balances, or approving requests, I've got you covered."}]
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt := st.chat_input("Say something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)     
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
                    pass
            st.session_state.messages.append(message)
            
    #-----------------------------------------------------------------------------------------------------------------------------------   
    def PerformanceEvaluation():
        st.header("Performance Evaluation")
        st.write("---")
        
        #chatgpt
        # Store generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Hello there! I'm JAVIS, your friendly virtual assistant, at your service! Evaluating employee performance made easy! Tell me about your performance evaluation criteria, and I'll assist you in gathering and analyzing relevant data for fair and insightful assessments."}]
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt := st.chat_input("Say something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)     
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
                    pass
            st.session_state.messages.append(message)
    
    #-----------------------------------------------------------------------------------------------------------------------------------
    def SalaryandBenefitsManagement():
        st.header("Salary and Benefits Management")
        st.write("---")
        
        #chatgpt
        # Store generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Hello there! I'm JAVIS, your friendly virtual assistant, at your service! Curious about salary and benefits information? I'm here to provide comprehensive assistance, from salary inquiries to benefit updates, ensuring transparency and clarity."}]
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt := st.chat_input("Say something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)     
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
                    pass
            st.session_state.messages.append(message)
    
    #-----------------------------------------------------------------------------------------------------------------------------------
    def ReportingandAnalytics():
        st.header("Reporting and Analytics")
        st.write("---")
        
        #chatgpt
        # Store generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Hello there! I'm JAVIS, your friendly virtual assistant, at your service! Unlock valuable insights with my reporting and analytics capabilities! Whether you need customized reports or data analysis, I'll crunch the numbers and deliver actionable information tailored to your needs."}]
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt := st.chat_input("Say something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)     
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Uhhmm... let me think for a moment. Please bear with me."):
                    pass
            st.session_state.messages.append(message)
    
    #-----------------------------------------------------------------------------------------------------------------------------------        
    with st.sidebar:
        selected = option_menu("Main Menu",["Employee Information Management", "Attendance Tracking", "Leave Management","Performance Evaluation","Salary and Benefits Management","Reporting and Analytics"],
                                icons=["bi bi-person-fill", "bi bi-calendar-check-fill", "bi bi-clipboard-check", "bi bi-bar-chart-fill","bi bi-currency-dollar","bi bi-graph-up"],menu_icon="cast", default_index=0)
    if selected == "Contact":
        show_contact()
    elif selected == "Employee Information Management":
        EmployeeInformationManagement()
    elif selected == "Attendance Tracking":
        AttendanceTracking()
    elif selected == "Leave Management":
        LeaveManagement()
    elif selected == "Performance Evaluation":
        PerformanceEvaluation()
    elif selected == "Salary and Benefits Management":
        SalaryandBenefitsManagement()
    elif selected == "Reporting and Analytics":
        ReportingandAnalytics()

#-----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()