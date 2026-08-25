import json

from rakunlib.rakun_plugin import RakunPlugin
from rakunlib.rakun_response import PluginResult


@RakunPlugin.runifmain(__name__, __file__)
class RktSimplePlugin(RakunPlugin):
    def __init__(self) -> None:
        module_dir_name = __file__.split("/")[-1].replace(".py", "")
        super().__init__(module_dir_name)

    def resolve(
        self,
        search: str,
        search_type: str,
        profile: dict | None,
        media_dir: str,
        data_dir: str,
        plugin_dir: str,
        plugin_id: str,
        is_install: bool,
        is_test: bool,
    ) -> dict:

        # create a plugin result object, which will be returned to the core.
        plugin_result = PluginResult()

        # Simulate an api response as json string, which can then be displayed in the frontend as raw data example.
        raw_data_example = json.dumps(
            {
                "search": search,
                "search_type": search_type,
            }
        )

        plugin_result.set_message(
            "This is an example of an optional informational message.", level="info"
        )
        plugin_result.set_raw(data=raw_data_example, type="json")

        # In this example, we simulate a request with results, so we need a main_view, which can then have one or many boxes.
        # Create a box where the results are displayed.
        main_view = plugin_result.create_main_view()
        box = main_view.create_box("Searched data")
        box.add_text_section("Your search", search)
        box.add_text_section("Search type", search_type)

        # return a serialized plugin result to the core
        return plugin_result.serialize()
