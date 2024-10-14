import fpdf
import csv

# function that turns a line from a csv file into a pdf
def csv_to_pdf(line):
    pdf = fpdf.FPDF(format="letter")
    pdf.add_page()
    pdf.set_font("Times", "B", 16)
    title = line[0].encode('latin1', 'replace').decode('latin1')
    pdf.cell(0, 10, title, ln=True, align='C')

    pdf.set_font("Times", "I", 12)
    author_date = (f'{line[1]} {line[3]}').upper().encode('latin1', 'replace').decode('latin1')
    pdf.cell(0, 10, author_date, ln=True, align='C')
    pdf.ln(20)  

    pdf.set_font("Times", "", 12)
    content = line[4].encode('latin1', 'replace').decode('latin1')
    for content_line in content.split("\n"):
        pdf.multi_cell(0, 10, content_line)
    
    filename = f"{line[2]} : {line[0]}.pdf".encode('latin1', 'replace').decode('latin1')
    pdf.output(f"pdfs/{filename}")

# main function
def main():
    with open('stored_data/articles.csv') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the first line (header)
        for line in reader:
            csv_to_pdf(line)
            break

if __name__ == "__main__":
    main()