from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Global Health Data Analyzer: User Guide', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def create_pdf(input_file, output_file):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', '', 11)

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                pdf.ln(5)
                continue
            
            # Very basic markdown parsing
            if line.startswith('## '):
                pdf.set_font('Arial', 'B', 14)
                # Remove markdown formatting
                line = line.replace('##', '').strip()
                pdf.multi_cell(0, 10, line)
                pdf.set_font('Arial', '', 11)
            elif line.startswith('### '):
                pdf.set_font('Arial', 'B', 12)
                line = line.replace('###', '').strip()
                pdf.multi_cell(0, 8, line)
                pdf.set_font('Arial', '', 11)
            else:
                # Remove bold marks 
                line = line.replace('**', '')
                pdf.multi_cell(0, 6, line)

    pdf.output(output_file, 'F')
    print(f"Created {output_file}")

if __name__ == '__main__':
    create_pdf('User_Guide.md', 'Global_Health_Data_Analyzer_Guide.pdf')
