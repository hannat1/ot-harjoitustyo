## HSL-matkakortti, sekvenssikaavio

sequenceDiagram
    Main->>+ laitehallinto: HKLLaitehallinto()
    Main->>+ rautatietori: Lataajalaite()
    Main->>+ ratikka6: Lukijalaite()
    Main->>+ bussi244: Lukijalaite()
    Main-->>+laitehallinto:lisaa_lataaja(rautatietori)
