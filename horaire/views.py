import os
from pathlib import Path
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from anneeAcademiques.models import AnneeAcademique
from horaire.Horaire import PDF
from cours.models import Attribuer, Cours, Dispenser
from section.models import Departement, Section, Secretaire_section
from horaire.Horaire import firstDay, lastDay
from promotions.models import Promotion
from salles.models import Salle
from users.models import Enseignant, Etudiant
from django.utils import timezone
from django.db.models import Q
from slugify import slugify
from .Horaire import PDF
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter


def makeHoraire():
    anneeAcademique_now = AnneeAcademique.objects.all().order_by("-id")
    print(anneeAcademique_now)
    if anneeAcademique_now.exists():
        anneeAcademique_now = anneeAcademique_now[0]
        horaires = Dispenser.objects.filter(
            anneeAcademique=anneeAcademique_now
        ).order_by("-date")
        if horaires.exists():
            vacations = ["Jour", "Soir"]
            path = []
            for vacation in vacations:
                promotions = Promotion.objects.filter(actif=True).order_by(
                    "designation"
                )
                departements = Departement.objects.all().order_by("designation")
                horaire = PDF(
                    Dispenser,
                    Attribuer,
                    departements,
                    promotions,
                    Enseignant,
                    Cours,
                    Salle,
                    anneeAcademique_now.id,
                    vacation,
                    "L",
                    "mm",
                    "Letter",
                )
                horaire.set_title("HORAIRE DE LA SEMAINE")
                horaire.set_author("UNIC - BUKAVU")
                horaire.alias_nb_pages()
                horaire.add_page()
                horaire.set_auto_page_break(auto=True, margin=5)
                horaire.body()
                media_path = os.path.join(
                    settings.MEDIA_ROOT,
                    f"horaire_{vacation}{timezone.now().date()}.pdf",
                )
                horaire.output(media_path)
                path.append(media_path)
            return path
        return False
    return False


class Horaire(View):
    # permission_classes = [IsAuthenticated]
    BASE_DIR = Path(__file__).resolve().parent.parent

    def get(self, request):
        pdf_writer = PdfWriter()
        rs = makeHoraire()
        if rs:
            for path in rs:
                pdf = PdfReader(path)
                for i in range(len(pdf.pages)):
                    page = pdf.pages[i]
                    pdf_writer.add_page(page)
            pdf_writer.write("media/horaires.pdf")
            # return JsonResponse({"success": request.build_absolute_uri('/media/horaires.pdf')})
            return FileResponse(
                open(f"{self.BASE_DIR}/media/horaires.pdf", "rb"),
                content_type="application/pdf",
            )
        return JsonResponse(
            {"fail": "Pas d'année academique disponible ou pas d'horaire élaborée"}
        )


class HoraireWeek(TemplateView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        now = timezone.now().date()
        horaires = Dispenser.objects.filter(
            Q(date__lte=lastDay(now)) & Q(date__gte=firstDay(now))
        )
        return JsonResponse({"horaires": horaires})
