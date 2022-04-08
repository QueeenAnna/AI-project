************************************************************************************************************************************************
### <Mall för daily standup>

## Daily 2022-xx-xx

## Närvarande: 

### Anna
*   __Vad har jag gjort sedan avstämningen igår?__

*   __Vad ska jag göra till nästa avstämning?__

*   __Behöver jag hjälp med något?__

### Elvir
*   __Vad har jag gjort sedan avstämningen igår?__

*   __Vad ska jag göra till nästa avstämning?__

*   __Behöver jag hjälp med något?__


### MaryAnn
*   __Vad har jag gjort sedan avstämningen igår?__

*   __Vad ska jag göra till nästa avstämning?__

*   __Behöver jag hjälp med något?__


### Johanna
*   __Vad har jag gjort sedan avstämningen igår?__

*   __Vad ska jag göra till nästa avstämning?__

*   __Behöver jag hjälp med något?__

### Övrigt
*

************************************************************************************************************************************************

### <Mall för sprint review och sprint planning>

## Möte 2022-xx-xx

### Sprint review
* Blev alla issues klara?
   - Om inte, varför?
* Icke klara issues återförs till backlog, efter att de har uppdaterats.
  - Har vissa delar klarats av?
  - Skall vi ha en ny tidsuppskattning?
  - Vad behövs för att vi skall klara detta issue nästa gång?
* Har det kommit upp nya saker som skall läggas till på er backlog?
* Bedöm vad ni kan göra bättre i nästa sprint


### Sprint planning
* Beskriv det övergripande målet med sprinten:
  -Namn:
  -Beskrivning:
  -Startdatum:
  -Slutdatum:
  -Backlogg: Se Time_estimates.txt
* Uppskatta tillgänglig tid för gruppen i nästa sprint.
* Vad ska ingå i nästa veckas sprint?


************************************************************************************************************************************************
## Daily 2022-04-08

### Närvarande: Johanna, MaryAnn, Elvir och Anna

### Anna
*   __Vad har jag gjort sedan avstämningen igår?__
    Analyserade och rensade RAW_recipies datasetet till de columner som är intressanta för oss. Analyserade och diskuterade med gruppen och fick en tydligre bild på hur prjekten ska läggas upp. Lagt till dem första issuesen i project backlog. Läste på om OpenCV och lärde sig de grundläggande delarna. 

*   __Vad ska jag göra till nästa avstämning?__
    Forsätta läsa på om OpenCV och börja titta på CNN. Ta reda på vilka delar som behövs för att kunna bygga en kamera detector.

*   __Behöver jag hjälp med något?__
    Nej

### Elvir
*   __Vad har jag gjort sedan avstämningen igår?__
    Analyserade och rensade RAW_recipies datasetet till de columner som är intressanta för oss. Analyserade och diskuterade med gruppen och fick en tydligre bild på hur prjekten ska läggas upp. Lagt till dem första issuesen i project backlog. Läste på om OpenCV och lärde sig de grundläggande delarna.
    
*   __Vad ska jag göra till nästa avstämning?__
    Forstätta upplysa sig själv med OpenCV och börja titta på CNN.

*   __Behöver jag hjälp med något?__
    Nej

### MaryAnn
*   __Vad har jag gjort sedan avstämningen igår?__
    Analyserade och diskuterade med gruppen och fick en tydligre bild på hur prjekten ska läggas upp. Lagt till dem första issuesen i project backlog.
    Läste på om OpenCV, hittade exempelkod som uppfyller det vi vill ha. Exemplekoden handlade om om face/object recognition.
    
*   __Vad ska jag göra till nästa avstämning?__
    Analysera exempelkoden i c++ och vidare kanske försöka översätta koden till python. Fortstätta upplysa sig själv med OpenCV och börja titta på hur man kan bygga en open shape.
    
*   __Behöver jag hjälp med något?__
    Nej

### Johanna
*   __Vad har jag gjort sedan avstämningen igår?__
    Vabbat. Analyserade och diskuterade med gruppen och fick en tydligre bild på hur prjekten ska läggas upp. Lagt till dem första issuesen i project backlog. 

*   __Vad ska jag göra till nästa avstämning?__
    Vabba och läsa på om OpenCV så gott det går.
    
*   __Behöver jag hjälp med något?__
    Nej
    
### Övrigt
*

************************************************************************************************************************************************
## Daily 2022-04-07

### Närvarande: Anna, Elvir, MaryAnn, Johanna
      Vi hade vårt första projektmöte igår och bestämde formerna för samarbetet; tid (gemensam tid 9-15 alla veckodagar förutom lektionsdagar), plats (tillsammans
      på skolan för de som har möjlighet till en början för att få en gemensam och enhetlig syn på projektet och sedan kommer vi eventuellt successivt att övergå 
      till distans), plattform (GitHub), kommunikationskanal (Discord) samt att vi ska försöka parprogrammera i så stor utsträckning som möjligt. Mohammad som ingår
      i vår grupp var inte med igår, vi hjälper honom att komma in i arbetet så bra vi kan när vi fått tag på honom. 
      
      Några förslag på projekt kom upp och vi landade till slut i en applikation där vi med hjälp av mobilen ska scanna eller filma de grönsaker (initialt, kanske att 
      fler livsmedelsgrupper tillkomer senare i projektet) som finns där och sedan ska vår applikation leta upp recept som innehåller dessa ingredienser. Vi fick lite
      input från Joakim och då kom följande frågeställningar/saker att tänka på upp:
      1. Grönsaker kan vara förvarade i förpackningar, hur hanterar vi det?
      2. Hur vet vi mängden av varje grönsakstyp?
      3. Vi börjar med t.ex. tomat och gurka som är skilda till färg och form och lägger till andra grönsaker efterhand. Kanske någon som liknar (ex. rödlök).
      4. Ska vi försöka hålla reda på vilket recept som applikation har föreslagit så att vi inte får samma förslag om och om igen?
      5. Ska användaren kunna ge betyg på receptet och låta de med högt betyg återkomma efter ett visst tidsintervall?
      6. Vi kan själva ta kort på grönsakerna, måste inte använda dataset. Viktigt då att ta kort med olika avstånd, antal, vinklar, belysning, bakgrund, mognadsgrad 
         m.m.
      7. Ska vi ha en kategori som heter "Annan grönsak"?
      8. Hur kopplar vi ihop grönsakerna som vi identifierat med receptet? Ska ingrediensen förekomma enbart i ingredienslistan eller även i fritexten?
      9. Vissa kylskåp har blått ljus, hår påverkar det möjligheten att identifiera grönsakerna?
      10. Joakim tipsade om att använda CNN, convolutional neural network för att känna igen grönsakerna samt cv2 för att "fiffla med bilderna" (finns i opencv-
          python), t.ex. att lägga konturer hur lång eller bred en grönsak är för att lättare identifiera objektet.
          

          
### Anna
*   Vad har jag gjort sedan avstämningen igår?
     Skapat ett repo på GitHub och delat med gruppen.
*   Vad ska jag göra till nästa avstämning?
      Kolla dataseten. Läsa på om opencv och eventuellt CNN.
*   Behöver jag hjälp med något?
      Nej

### Elvir
*   Vad har jag gjort sedan avstämningen igår?
      Gjort mallen för kanban i GitHub. Letade upp ett dataset med frukter och grönsaker.
*   Vad ska jag göra till nästa avstämning?
      Kolla dataseten. Läsa på om opencv och eventuellt CNN.
*   Behöver jag hjälp med något?
      Nej

### MaryAnn
*   Vad har jag gjort sedan avstämningen igår?
*   Vad ska jag göra till nästa avstämning?
      Kolla dataseten. Läsa på om opencv och eventuellt CNN.
*   Behöver jag hjälp med något?


### Johanna
*   Vad har jag gjort sedan avstämningen igår?
      Hittade ett dataset med recept. Har kollat vidare på andra dataset med bilder på grönsaker som ska komplettera det Elvir hittade. Inget att fortsätta med just 
      nu, kanske att det blir aktuellt senare. 
*   Vad ska jag göra till nästa avstämning?
      Kolla dataseten. Läsa på om opencv och eventuellt CNN.
*   Behöver jag hjälp med något?
      Nej

### Övrigt
*     Då det är så mycket nytt att läsa in sig på och vi inte riktigt vet vilka issues som vi kommer att behöva göra väntar vi med att göra en sprint backlog tills
      vi har mer koll på ämnet, troligtvis på måndag.

************************************************************************************************************************************************
