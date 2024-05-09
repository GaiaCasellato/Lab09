import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        distanza = int(self._view._txtIn.value)
        self._model.buildGraph()
        self._view._txt_result.controls.clear()
        for connessione in self._model.rotte:
             if int(connessione.avg_distance) > distanza:
                self._model.fillGraph(connessione.origin_airport_id, connessione.destination_airport_id)

        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo  è stato creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nEdges} archi."))
        for connessione in self._model.rotte:
            if int(connessione.avg_distance) > distanza:
                grafo_bellino = self._model.fillGraph(connessione.origin_airport_id, connessione.destination_airport_id)
                for i in grafo_bellino:
                    self._view._txt_result.controls.append(ft.Text(i))
        self._view.update_page()



