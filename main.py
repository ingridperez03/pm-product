def initApp(App):
    App = Aplicacio()
    dimensioDemografica = initDemografica()
    App.afegirDimensio("Demogràfica", dimensioDemografica)

if __name__ == "__main__":
    initApp()
