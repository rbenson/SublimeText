import sublime, sublime_plugin

class ToggleCenteredCommand(sublime_plugin.WindowCommand):
  def run(self):
    v = self
    if v.view.settings().get('draw_centered') == 'False':
      v.view.settings().set('draw_centered',True)
    else:
     v.view.settings().set('draw_centered',False)
