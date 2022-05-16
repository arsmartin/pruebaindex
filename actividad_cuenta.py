class Cuenta:
  def __init__ (self, titular, cantidad):
      self.titular=titular
      self.cantidad=cantidad

  def mostrar(self):
      print(f"Titular de la cuenta:\n {self.titular} \n\nSaldo de la cuenta:\n $", float(self.cantidad))
 
  def ingresar(self, ingreso):
      self.ingreso = ingreso
      print("\nDEPÓSITO.")
      if ingreso>0:
        self.cantidad+=self.ingreso
        print("Ingresó $",float(self.ingreso), "a su cuenta. \nSu saldo es de:\n", float(self.cantidad))
      elif ingreso <=0:
        print("No ha ingresado ningún monto. \nSu saldo es de:\n $", float(self.cantidad))
 
  def retirar(self, retiro):
      self.retiro = retiro
      self.cantidad-=self.retiro
      print("\nEXTRACCIÓN.")
      if retiro>0:
        print("Retiró $", float(self.retiro), "de su cuenta. \nSu saldo es de:\n $", float(self.cantidad))
      elif retiro<=0:
        print(f"No retiró dinero. \nSu saldo es de:\n $", float(self.cantidad))
      
usuario1 = Cuenta("Martín Arias", 1000)
usuario1.mostrar()
usuario1.ingresar(30)
usuario1.retirar(0)