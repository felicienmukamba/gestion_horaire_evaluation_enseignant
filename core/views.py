from cours.models import Attribuer, Dispenser
from django.views.generic import TemplateView
from horaire.views import makeHoraire
from salles.models import Salle
from section.models import Secretaire_section, Section
from users.models import Enseignant, Etudiant
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from django.shortcuts import render


def home(request):
    pdf_writer = PdfWriter()
    rs = makeHoraire()
    if rs:
        for path in rs:
            pdf = PdfReader(path)
            for i in range(len(pdf.pages)):
                page = pdf.pages[i]
                pdf_writer.add_page(page)
        pdf_writer.write("media/horaires.pdf")
    return render(
        request,
        "home/home.html",
        context={"horaire_url": request.build_absolute_uri("/media/horaires.pdf")},
    )


class DashbordView(TemplateView):
    template_name = "dashbord/dashbord.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)

        # Counts
        context["students_count"] = Etudiant.objects.all().count()
        context["enseignants_count"] = Enseignant.objects.all().count()
        context["salles_count"] = Salle.objects.all().count()
        context["secretaire_section_count"] = Secretaire_section.objects.all().count()
        context["sections_count"] = Section.objects.all().count()

        # Elements
        context["students"] = Etudiant.objects.all()
        context["enseignants"] = Enseignant.objects.all()
        context["salles"] = Salle.objects.all()
        context["secretaire_section"] = Secretaire_section.objects.all()
        context["sections"] = Section.objects.all()
        context["attributions"] = Attribuer.objects.all()
        context["dispensers"] = Dispenser.objects.all()

        return context

