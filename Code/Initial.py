BLACK = "#0A0A0A"
GREY = "#323232"
WHITE = "#FAFAFA"
D_RED = "#880000"
L_RED = "#FF0000"
D_GREEN = "#008800"
L_GREEN = "#00FF00"
D_BLUE = "#000088"
L_BLUE = "#0000FF"

FF = ("Helvetica", 20, "bold")

def button(btn, x, y, lc, dc, wc, w, h):
      def on_enter(e):
            btn['background'] = dc
            btn['foreground'] = wc
      def on_leave(e):
            btn['background'] = lc
        
      btn.bind("<Enter>", on_enter)
      btn.bind("<Leave>", on_leave)

      btn.config(bg=lc, fg=wc, activebackground=lc, activeforeground=wc)
      btn.config(font=FF,bd=0, width=w, height=h)
      btn.place(x=x, y=y)
