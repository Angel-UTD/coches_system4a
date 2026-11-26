from models import coches_model
from views import coches_view

class CochesController:
    
    def insertar_controller(self):
        coche1 = coches_model.cochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())                    
        coche1 = coches_model.cochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
        # self.insertar_view()

    def eliminar_controller(self):
        id=self.id.get()
        resp = self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta = coches_model.cochesModel.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)
        # self.eliminar_view()

    def modificar_controller(self):
        id=self.id.get()                     
        coche1 = coches_model.cochesModel(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
        # self.modificar_view()

    def consultar_controller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_model.cochesModel.consultar():
            self.tree.insert("", "end", values=row)

    def buscar_controller(self, tipo_accion):
        id = self.id.get()
        coche1 = coches_model.cochesModel.buscar(id)
        if len(coche1) > 0:
            coches_view.CochesView.encontrado(tipo_accion, coche1)
               
