
from rakunlib.rakun_plugin import RakunPlugin
from rakunlib.rakun_response import PluginResult

@RakunPlugin.runifmain(__name__, __file__)
class Badam(RakunPlugin):
    def __init__(self) -> None:
        module_dir_name = __file__.split("/")[-1].replace(".py", "")
        super().__init__(module_dir_name)

    def resolve(self,
                search: str,
                search_type: str,
                profile:dict | None,
                media_dir:str,
                data_dir:str,
                plugin_dir:str,
                plugin_id:str,
                is_install:bool,
                is_test:bool
                ) -> dict:

        plugin_result = PluginResult()
                

        # MainView
        main_view = plugin_result.create_main_view()

        box = main_view.create_box()
        box.title = "Box Title"
        box.add_text_section(title="Search", text=search)

        return plugin_result.serialize()
