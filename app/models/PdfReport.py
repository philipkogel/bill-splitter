from fpdf import FPDF
from .Household import Household


class PdfReport:
    """Creates a PDF file that contains data about split house payment."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self, household: Household):
        print(f'-------- Generating {self.filename} ----------')
        pdf = FPDF()
        pdf.add_page()

        # Add icon
        pdf.image('assets/house.png', w=15, h=15)

        # Title
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=0, h=20, txt='Household Bill', border=0, align="C", ln=1)

        # Amount and period
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=50, h=5, txt='Amount:', border=0)
        pdf.cell(w=0, h=5, txt=str(household.bill.amount), border=0, ln=1)
        pdf.cell(w=50, h=10, txt='Period:', border=0)
        pdf.cell(w=0, h=10, txt=household.bill.period.strftime('%B %Y'), border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        # Flatmates
        for flatmate in household.flatmates:
            pdf.cell(w=30, h=5, txt=flatmate.name, border=0)
            pdf.cell(w=20, h=5, txt=f'{str(flatmate.days_in_house)} days', border=0)
            pdf.cell(
                w=0,
                h=5,
                txt=str(
                    round(
                        flatmate.pays(
                            bill=household.bill,
                            household_days_sum=household.sum_days_in()
                        ), 2)),
                border=0,
                ln=1
            )

        pdf.output(f'files/{self.filename}')
        print(f'-------- {self.filename} is ready! ----------')