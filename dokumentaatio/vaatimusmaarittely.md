# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on hirsipuu-peli. Pelissä on yksi pelaaja, joka pyrkii arvaamaan annetun sanan syöttämällä kirjaimia yksi kerrallaan. 

## Käyttäjät

Pelissä on vain yksi käyttäjä. Sovellusta laajennettaessa voitaisiin lisätä hallinnoiva käyttäjä, joka voisi esimerkiksi lisätä omia sanoja peliin. 

## Toiminnallisuus

### Aloitus

Pelaaja voi aloittaa pelin. Peli generoi jonkin sanan (50 sanamahdollisuutta), jonka pituus näkyy näytöllä viivoina. 

### Pelaaminen
Pelaaja syöttää jonkin kirjaimen. Jos kirjain on sanassa, tulee kaikki kyseiset kirjaimet näkyviin. Jos kirjain ei ole sanassa, hirttomies-kuvaan tulee yksi elementti lisää.
Samaa kirjainta ei voi syöttää enempää kuin yhden kerran. Hirttomies kuvassa on 6 elementtiä. 6 kirjainta saa siis mennä väärin, ennen kuin pelaaja häviää. 

### Pelin päättyminen
Jos pelaaja saa koko sanan arvattua ennen kuin hirttomies-kuva on valmis, pelaaja voittaa. Jos hirttomies on valmis ennen kuin sana on kokonaan arvattu, pelaaja häviää. 
Pelaajalla saa siis mennä 6 kirjainta väärin, ennen kuin pelaaja häviää. 

## Jatkokehitysideoita
Peliä voisi laajentaa niin, että pelaajalla on aikaraja. 
Pelissä voisi olla mahdollisuus itse lisätä sanoja peliin. 
Pelissä voisi olla solo-pelin lisäksi duo-peli, jossa vuorotellen pelaajat valitsisivat toiselle pelaajalle sanan jota arvata. 


