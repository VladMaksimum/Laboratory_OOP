from Injector import Injector
import Examples
from PerRequest import PerRequest
from Scoped import Scoped
from Singleton import Singleton
from Scope import Scope

dep_inj_1 = Injector()
dep_inj_1.register(Examples.Database, Examples.SQLDB, PerRequest, params=["connection_str"])
dep_inj_1.register(Examples.Logger, Examples.FileLogger, Singleton)
dep_inj_1.register(Examples.MailService, Examples.GmailService, Scoped)

dep_inj_2 = Injector()
dep_inj_2.register(Examples.Database, Examples.MongoDB, PerRequest)
dep_inj_2.register(Examples.Logger, Examples.ConsoleLogger, Singleton)
dep_inj_2.register(Examples.MailService, Examples.YmailService, Scoped)


print(f'Created {dep_inj_1.get_instance(Examples.Database)} by dep_inj_1')
print(f'Created {dep_inj_1.get_instance(Examples.Database)} by dep_inj_1')
print(f'Created {dep_inj_2.get_instance(Examples.Database)} by dep_inj_2')
print(f'Created {dep_inj_2.get_instance(Examples.Database)} by dep_inj_2')

print(f'\nCreated {dep_inj_1.get_instance(Examples.Logger)} by dep_inj_1')
print(f'Created {dep_inj_1.get_instance(Examples.Logger)} by dep_inj_1')
print(f'Created {dep_inj_2.get_instance(Examples.Logger)} by dep_inj_2')
print(f'Created {dep_inj_2.get_instance(Examples.Logger)} by dep_inj_2')

with Scope(dep_inj_1):
    print(f'\nCreated {dep_inj_1.get_instance(Examples.MailService)} by dep_inj_1')
    print(f'Created {dep_inj_1.get_instance(Examples.MailService)} by dep_inj_1')

print(f'\nCreated {dep_inj_1.get_instance(Examples.MailService)} by dep_inj_1')
print(f'Created {dep_inj_1.get_instance(Examples.MailService)} by dep_inj_1')

with Scope(dep_inj_2):
    print(f'\nCreated {dep_inj_2.get_instance(Examples.MailService)} by dep_inj_2')
    print(f'Created {dep_inj_2.get_instance(Examples.MailService)} by dep_inj_2')


#dep_inj_1.register(Examples.I1, Examples.C1, PerRequest)
dep_inj_1.register(Examples.I2, Examples.C2, PerRequest, ["i1"])

#print(f'\nCreated {dep_inj_1.get_instance(Examples.I2, params={"i1": dep_inj_1.get_instance(Examples.I1)})} by dep_inj_1')

print(dep_inj_1.get_instance(Examples.Database, params={"connection_str": "test"}).connection_str)