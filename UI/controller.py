import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDYears(self):

        years = self._model.getAllYears()

        for year in years:
            self._view._ddYear1.options.append(
                ft.dropdown.Option(year)
            )

        for year in years:
            self._view._ddYear2.options.append(
                ft.dropdown.Option(year)
            )
        self._view.update_page()

    def handleBuildGraph(self, e):

        self._view._txtGraphDetails.controls.clear()

        if self._view._ddYear1.value is None:
            self._view.create_alert("Scegli un anno di partenza")
            self._view.update_page()
            return

        if self._view._ddYear2.value is None:
            self._view.create_alert("Scegli un anno di fine")
            self._view.update_page()
            return

        if self._view._ddYear1.value > self._view._ddYear2.value:
            self._view.create_alert("L'anno di fine deve essere maggiore o uguale all'anno di inizio")
            self._view.update_page()
            return

        self._model.creaGrafo(self._view._ddYear1.value, self._view._ddYear2.value)

        if len(self._model._grafo) == 0:
            self._view.create_alert("Il grafo non è stato creato correttamente")
            self._view.update_page()
            return

        self._view._txtGraphDetails.controls.append(
            ft.Text(f"Grafo correttamente creato.")
        )

        nNodi, nArchi = self._model.getDettagliGrafo()

        self._view._txtGraphDetails.controls.append(
            ft.Text(f"Il grafo contiene {nNodi} e {nArchi}")
        )

        self._view.update_page()

    def handlePrintDetails(self, e):

        if len(self._model._grafo) == 0:
            self._view.create_alert("Crea prima il grafo")
            self._view.update_page()
            return

        compConn = self._model.getCompConn()

        for i, val in compConn:
            self._view._txtGraphDetails.controls.append(
                ft.Text(f"{i.name} -- {val}")
            )

        self._view.update_page()



    def handleCercaDreamChampionship(self, e):
        pass


