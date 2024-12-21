import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox


class EXEPackager:
    def __init__(self, root):
        self.root = root
        self.root.title("EXE Packager")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.files = []

        # Label
        tk.Label(root, text="EXE Packager", font=("Arial", 16)).pack(pady=10)

        # Listbox to display files
        self.file_listbox = Listbox(root, width=60, height=15)
        self.file_listbox.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add EXE", width=12, command=self.add_file).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Remove Selected", width=15, command=self.remove_selected).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Package EXEs", width=15, command=self.package_exes).grid(row=0, column=2, padx=5)

        # Exit Button
        tk.Button(root, text="Exit", width=12, command=root.quit).pack(pady=10)

    def add_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if file_path and file_path not in self.files:
            self.files.append(file_path)
            self.update_listbox()

    def remove_selected(self):
        selected_indices = self.file_listbox.curselection()
        for index in selected_indices[::-1]:  # Reverse to prevent index shifting issues
            del self.files[index]
        self.update_listbox()

    def update_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.files:
            self.file_listbox.insert(tk.END, os.path.basename(file))

    def package_exes(self):
        if not self.files:
            messagebox.showerror("Error", "No EXE files selected.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".exe", filetypes=[("Executable files", "*.exe")])
        if not output_file:
            return

        # Create a script to run the combined EXEs
        launcher_script = os.path.join(os.getcwd(), "launcher.py")
        with open(launcher_script, "w") as script_file:
            script_file.write("import os\n")
            script_file.write("import subprocess\n\n")
            script_file.write("def main():\n")
            script_file.write("    exes = [\n")
            for file in self.files:
                script_file.write(f"        r'{file}',\n")
            script_file.write("    ]\n")
            script_file.write("    print('Select an executable to run:')\n")
            script_file.write("    for idx, exe in enumerate(exes, start=1):\n")
            script_file.write("        print(f'{idx}. {os.path.basename(exe)}')\n")
            script_file.write("    choice = int(input('Enter choice: '))\n")
            script_file.write("    if 1 <= choice <= len(exes):\n")
            script_file.write("        subprocess.run(exes[choice - 1])\n")
            script_file.write("\nif __name__ == '__main__':\n")
            script_file.write("    main()\n")

        # Package into an EXE
        os.system(f"pyinstaller --onefile --name '{os.path.basename(output_file)}' '{launcher_script}'")

        # Clean up
        os.remove(launcher_script)
        build_dir = os.path.join(os.getcwd(), "build")
        dist_dir = os.path.join(os.getcwd(), "dist")
        spec_file = os.path.join(os.getcwd(), "launcher.spec")
        if os.path.exists(build_dir):
            os.rmdir(build_dir)
        if os.path.exists(spec_file):
            os.remove(spec_file)

        messagebox.showinfo("Success", f"Packaged EXEs into {output_file}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EXEPackager(root)
    root.mainloop()
