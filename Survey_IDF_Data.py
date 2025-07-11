# # import streamlit as st
# # import pandas as pd
# # import os

# # # Define the file paths
# # input_file = r'D:\A\DAILY REPORTS\Shailendra_Sir_Project\IDF_ACCT_ID.csv'
# # output_file = r'D:\data_extract_to_python\BILLED_09_07_2025.csv'

# # # Check if file exists
# # if not os.path.exists(input_file):
# #     print(f"❌ File not found: {input_file}")
# # else:
# #     print("✅ File found. Processing...")

# # # Load data
# # df = pd.read_csv(input_file)

# # # 🧾 Title and description of the Streamlit form
# # st.title("Supervisor Field Survey – IDF Cases")

# # # 📝 Caption providing instructions for users
# # st.caption("Please fill this form after on-site verification of IDF accounts.")

# # acct_id_input = st.text_input("**ENTER ACCT_ID**")

# # if acct_id_input:
# #     # Filter matching row
# #     match = df[df["ACCT_ID"].astype(str) == acct_id_input.strip()]
    
# #     if not match.empty:
# #         st.success("✅ ACCT_ID matched. Details below:")

    
# #         # ✅ Define fields to show
# #         fields = {
# #             "ZONE": match.iloc[0]["ZONE"],
# #             "CIRCLE": match.iloc[0]["CIRCLE"],
# #             "DIVISION": match.iloc[0]["DIVISION"],
# #             "SUB-DIVISION": match.iloc[0]["SUB-DIVISION"]
# #         }

# #         # ✅ Display in one row using columns
# #         cols = st.columns(len(fields))
# #         for col, (label, value) in zip(cols, fields.items()):
# #             col.markdown(
# #                 f"<span style='font-weight:600;'>{label}:</span><br>{value}",
# #                 unsafe_allow_html=True
# #             )
# #     else:
# #         st.error("❌ ACCT_ID not found. Please check and try again.")


# import streamlit as st
# import pandas as pd
# import os

# # Define the file paths
# input_file = r'D:\A\DAILY REPORTS\Shailendra_Sir_Project\IDF_ACCT_ID.csv'
# output_file = r'D:\data_extract_to_python\BILLED_09_07_2025.csv'

# # Check if file exists
# if not os.path.exists(input_file):
#     st.error(f"❌ File not found: {input_file}")
#     st.stop()

# # Load data
# df = pd.read_csv(input_file)

# # 🧾 Title and description of the Streamlit form
# st.title("Supervisor Field Survey – IDF Cases")
# st.caption("Please fill this form after on-site verification of IDF accounts.")

# # ACCT_ID input
# acct_id_input = st.text_input("**ENTER ACCT_ID**")

# if acct_id_input:
#     # Filter matching row
#     match = df[df["ACCT_ID"].astype(str) == acct_id_input.strip()]
    
#     if not match.empty:
#         st.success("✅ ACCT_ID matched. Details below:")

#         # ✅ Define fields here, only when match is found
#         fields = {
#             "ZONE": match.iloc[0]["ZONE"],
#             "CIRCLE": match.iloc[0]["CIRCLE"],
#             "DIVISION": match.iloc[0]["DIVISION"],
#             "SUB-DIVISION": match.iloc[0]["SUB-DIVISION"]
#         }

#         # ✅ Create columns inside the same block
#         cols = st.columns(len(fields))
#         for col, (label, value) in zip(cols, fields.items()):
#             col.markdown(
#                 f"<span style='font-weight:bold;'>{label}:</span><br>{value}",
#                 unsafe_allow_html=True
#             )
#     else:
#         st.error("❌ ACCT_ID not found. Please check and try again.")

import streamlit as st
import pandas as pd
import os

# --- File Paths ---
input_file = r'D:\A\DAILY REPORTS\Shailendra_Sir_Project\IDF_ACCT_ID.csv'
output_file = r'D:\data_extract_to_python\BILLED_09_07_2025.csv'

# --- File Existence Check ---
if not os.path.exists(input_file):
    st.error(f"❌ File not found: {input_file}")
    st.stop()

# --- Load Data ---
df = pd.read_csv(input_file)

# --- Title & Instructions ---
st.title("Supervisor Field Survey – IDF Cases")
st.caption("Please fill this form after on-site verification of IDF accounts.")

# --- Enter ACCT_ID ---
acct_id_input = st.text_input("**ENTER ACCT_ID**")

if acct_id_input:
    match = df[df["ACCT_ID"].astype(str) == acct_id_input.strip()]
    
    if not match.empty:
        st.success("✅ ACCT_ID matched. Details below:")

        # --- Display ZONE, CIRCLE etc. ---
        fields = {
            "ZONE": match.iloc[0]["ZONE"],
            "CIRCLE": match.iloc[0]["CIRCLE"],
            "DIVISION": match.iloc[0]["DIVISION"],
            "SUB-DIVISION": match.iloc[0]["SUB-DIVISION"]
        }

        cols = st.columns(len(fields))
        for col, (label, value) in zip(cols, fields.items()):
            col.markdown(f"<span style='font-weight:bold;'>{label}:</span><br>{value}", unsafe_allow_html=True)

        st.markdown("---")

        # --- Remark Dropdown ---
        remark_options = {
            "OK": ["METER SERIAL NUMBER", "METER IMAGE", "READING", "DEMAND"],
            "DEFECTIVE METER": ["METER SERIAL NUMBER", "METER IMAGE"],
            "LINE DISCONNECTED": ["METER SERIAL NUMBER", "METER IMAGE"],
            "NO METER AT SITE": ["PREMISES IMAGE"],
            "METER MIS MATCH": ["METER SERIAL NUMBER", "METER IMAGE", "METER READING", "DEMAND"],
            "HOUSE LOCK": ["PREMISES IMAGE"],
            "METER CHANGE NOT ADVISE": ["METER SERIAL NUMBER", "METER IMAGE", "METER READING", "DEMAND"],
            "PDC": ["METER IMAGE", "PREMISES IMAGE", "DOCUMENT RELATED TO PDC"]
        }

        selected_remark = st.selectbox("Select REMARK", list(remark_options.keys()))

        # --- Input Fields Based on Remark ---
        st.markdown("#### Enter Required Details:")
        input_data = {}
        for field in remark_options[selected_remark]:
            input_data[field] = st.text_input(f"{field}")

        # --- Submit Button ---
        if st.button("Submit"):
            # Save this input (append to file or process further)
            record = {
                "ACCT_ID": acct_id_input,
                "REMARK": selected_remark,
                **fields,
                **input_data
            }

            # Convert to DataFrame and append to CSV
            result_df = pd.DataFrame([record])

            if os.path.exists(output_file):
                result_df.to_csv(output_file, mode='a', header=False, index=False)
            else:
                result_df.to_csv(output_file, index=False)

            st.success("✅ Data submitted and saved successfully!")

    else:
        st.error("❌ ACCT_ID not found. Please check and try again.")


