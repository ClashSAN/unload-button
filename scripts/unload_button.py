import gradio as gr
import gc
from modules import sd_models,scripts,shared,sd_hijack,devices

class Script(scripts.Script):
    def title(self):
        return "Unload Button"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        unloadmodel = gr.Button(value="unload model",variant='primary')

        def unload():
            sd_hijack.model_hijack.undo_hijack(shared.sd_model)
            shared.sd_model = None
            gc.collect()
            devices.torch_gc()
            return

        unloadmodel.click(fn=unload)