import streamlit as st

from Email_Classification.Email_Classifier import classify_email
from Invoice_Extractor.Invoice_Text_Extractor import extract_text_from_pdf
from Comparator.Comparator_Main import compare_invoice_po

from RAG_Tool import policy_lookup



st.title("AR Dispute AI Assistant")

st.write("Upload email and documents to analyze dispute")


# EMAIL INPUT
email_text = st.text_area("Paste Email Content")


# FILE UPLOADS
invoice_file = st.file_uploader("Upload Invoice PDF", type=["pdf"])

po_file = st.file_uploader("Upload PO PDF", type=["pdf"])



if st.button("Process"):


    # STEP 1 EMAIL CLASSIFICATION
    st.write("## Step 1: Email Classification")

    email_result = classify_email(email_text)

    st.write(email_result)



    # STEP 2 INVOICE EXTRACTION
    if invoice_file:

        with open("temp_invoice.pdf", "wb") as f:

            f.write(invoice_file.read())


        st.write("## Step 2: Invoice Data")

        invoice_data = extract_text_from_pdf("temp_invoice.pdf")

        st.write(invoice_data)



    # STEP 3 PO EXTRACTION
    if po_file:

        with open("temp_po.pdf", "wb") as f:

            f.write(po_file.read())


        st.write("## Step 3: PO Data")

        po_data = extract_text_from_pdf("temp_po.pdf")

        st.write(po_data)



    # STEP 4 COMPARISON
    if invoice_file and po_file:

        st.write("## Step 4: Comparison Result")

        comparison = compare_invoice_po(

            invoice_data.model_dump(),

            po_data.model_dump()

        )

        st.write(comparison)



        # STEP 5 RAG POLICY LOOKUP
        # This is where RAG is used

        if comparison.amount_match == False:

            st.write("## Step 5: Policy Guidance")

            rag_answer = policy_lookup(

                "What is allowed tolerance for invoice amount mismatch?"

            )

            st.write(rag_answer)