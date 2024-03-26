## HSL-matkakortti, sekvenssikaavio

sequenceDiagram
    participant Main
    participant laitehallinto
    participant rautatietori
    participant ratikka6
    participant bussi244
    
    Main->>laitehallinto: HKLLaitehallinto()
    Main->>rautatietori: Lataajalaite()
    Main->>ratikka6: Lukijalaite()
    Main->>bussi244: Lukijalaite()
    Main->>laitehallinto:lisaa_lataaja(rautatietori)
    
