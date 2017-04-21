'''
storage = StorageFacade.for_provider('CloudMe') \
               .app_info_repository(app_info_repo) \
               .user_credentials_repository(user_credentials_repo) \
               .build()
quota = storage.get_quota()
print('User quota is:',quota)


storage = StorageFacade.for_provider('cloudme') \
               .app_info_repository(app_info_repo) \
               .user_credentials_repository(user_credentials_repo) \
               .build()
quota = storage.get_quota()
print('User quota is:',quota)

'''

#import storage
#from storage import IStorageProvider, register_provider
import CPath

class CloudMeStorage():

    PROVIDER_NAME = 'cloudme'

    def provider_name(self):
        print CloudMeStorage.PROVIDER_NAME

    def create_folder(self, c_path):
        if c_path.is_root():
            return False

        cm_root = self._load_folders_structure()
        cm_folder = cm_root.get_folder(c_path)
        if cm_folder:
            # folder already exists
            return False
        self._create_intermediary_folders(cm_root, c_path)
        return True

c=CloudMeStorage()
c.provider_name()
#c_path=None
value = c.create_folder(c_path)
print value


