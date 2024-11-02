from fpdf import FPDF
from dateutil.relativedelta import relativedelta

def addDay(date,days):
    return date+relativedelta(days=days)

def firstDay(date):
    dayOfWeek=date.weekday()
    return date-relativedelta(days=dayOfWeek)

def lastDay(date):
    dayOfWeek=date.weekday()
    offsetDays=5-dayOfWeek
    return date+relativedelta(days=offsetDays)

def format(date):
    return date.strftime("%d/%m/%Y")

class PDF(FPDF):
    def __init__(self,horaires,chargesHoraires,departements,promotions,enseignants,cours,salles,anneeAcademique,vacation,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.horaires=horaires
        self.chargesHoraires=chargesHoraires
        self.departements=departements
        self.promotions=promotions
        self.enseignants=enseignants
        self.cours=cours
        self.salles=salles
        self.vacation=vacation
        self.anneeAcademique=anneeAcademique
        last_horaire=self.horaires.objects.filter(anneeAcademique=self.anneeAcademique)[0]
        self.lundi=firstDay(last_horaire.date)
        self.mardi=addDay( self.lundi,1)
        self.mercredi=addDay( self.lundi,2)
        self.jeudi=addDay( self.lundi,3)
        self.vendredi=addDay( self.lundi,4)
        self.samedi=lastDay(last_horaire.date)
        
    def header(self):
        self.set_font('helvetica', '', 10)
        self.cell(0,5,'UNIC - BUKAVU',ln=1)
        self.set_font('helvetica', 'BU', 12)
        self.cell(0,5,f"HORAIRE DES COURS : SEMAINE DU LUNDI {format(self.lundi)} AU SAMEDI {format(self.samedi)} VACATION {self.vacation.upper()}",ln=1,align='C')
        self.ln(7)
        self.set_font('helvetica', '', 11)
        self.cell(32,7,'PROMOTIONS',border=1,align='C')
        self.cell(38,7,f'Lundi {format(self.lundi)}',border=1,align='C')
        self.cell(38,7,f'Mardi {format(self.mardi)}',border=1,align='C')
        self.cell(38,7,f'Mercredi {format(self.mercredi)}',border=1,align='C')
        self.cell(38,7,f'Jeudi {format(self.jeudi)}',border=1,align='C')
        self.cell(38,7,f'Vendredi {format(self.vendredi)}',border=1,align='C')
        self.cell(38,7,f'Samedi {format(self.samedi)}',border=1,align='C',ln=1)
                
    def body(self):
        self.set_font('helvetica', '', 10)
        for promotion in self.promotions:
             for departement in self.departements:
                departement_sigle=departement.designation
                if len(departement_sigle)>20:
                    departement_sigle=departement_sigle.replace('et ','').replace("de l'",'').replace("de ",'').replace(", ",'').split(' ')
                    departement_sigle=[word[0].upper() for word in departement_sigle]
                    departement_sigle='.'.join(departement_sigle)
                self.cell(32,12,f"{promotion.designation} {departement_sigle}",border=1,align='C')
                lundi=self.horaires.objects.filter(date=self.lundi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if lundi.exists():
                    cours=self.cours.objects.get(id=lundi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=lundi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=32
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=32
                    self.cell(38,4,f'{salle.designation}',border=1,align='C')
                else:
                    self.cell(38,4,f'',border=1,align='C',ln=1)
                    self.x+=32
                    self.cell(38,4,f'',border=1,align='C',ln=1)
                    self.x+=32
                    self.cell(38,4,'',border=1,align='C')
                mardi=self.horaires.objects.filter(date=self.mardi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if mardi.exists():
                    cours=self.cours.objects.get(id=mardi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=mardi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.y-=8
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=70
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=70
                    self.cell(38,4,f'{salle.designation}',border=1,align='C')
                else:
                    self.y-=8
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=70
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=70
                    self.cell(38,4,'',border=1,align='C')
                    
                mercredi=self.horaires.objects.filter(date=self.mercredi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if mercredi.exists():
                    cours=self.cours.objects.get(id=mercredi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=mercredi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.y-=8
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=108
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=108
                    self.cell(38,4,f'{salle.designation}',border=1,align='C')
                else:
                    self.y-=8
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=108
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=108
                    self.cell(38,4,'',border=1,align='C')
                
                jeudi=self.horaires.objects.filter(date=self.jeudi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if jeudi.exists():
                    cours=self.cours.objects.get(id=jeudi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=jeudi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.y-=8 
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=146
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=146
                    self.cell(38,4,f'{salle.designation}',border=1,align='C')
                else:
                    self.y-=8
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=146
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=146
                    self.cell(38,4,'',border=1,align='C')
                
                vendredi=self.horaires.objects.filter(date=self.vendredi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if vendredi.exists():
                    cours=self.cours.objects.get(id=vendredi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=vendredi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.y-=8  
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=184
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=184
                    self.cell(38,4,f'{salle.designation}',border=1,align='C')
                else:
                    self.y-=8
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=184
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=184
                    self.cell(38,4,'',border=1,align='C')
                
                samedi=self.horaires.objects.filter(date=self.samedi,anneeAcademique=self.anneeAcademique,vacation=self.vacation,departement=departement,promotion=promotion)
                if samedi.exists():
                    cours=self.cours.objects.get(id=samedi[0].cours.id)
                    chargeHoraire=self.chargesHoraires.objects.filter(cours=cours.id,anneeAcademique=self.anneeAcademique,promotion=promotion,departement=departement)
                    enseignant=self.enseignants.objects.get(id=chargeHoraire[0].enseignant.id)
                    salle=self.salles.objects.get(id=samedi[0].salle.id)
                    enseignant_noms=  enseignant.titreAcademique+' '+ enseignant.prenom+' '+ enseignant.nom if enseignant.prenom else  enseignant.titreAcademique+' '+enseignant.nom+' '+ enseignant.postnom
                    if len(enseignant_noms)>50:
                        enseignant_noms=enseignant_noms[0:50] 
                    self.y-=8 
                    self.cell(38,4,f'{cours.designation}',border=1,align='C',ln=1)
                    self.x+=222
                    self.cell(38,4,f'{enseignant_noms}',border=1,align='C',ln=1)
                    self.x+=222
                    self.cell(38,4,f'{salle.designation}',border=1,align='C',ln=1)
                else:
                    self.y-=8
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=222
                    self.cell(38,4,'',border=1,align='C',ln=1)
                    self.x+=222
                    self.cell(38,4,'',border=1,align='C',ln=1)
                   

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(169,169,169)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')
