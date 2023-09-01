namespace TextEditor
{
    public partial class frmEditor : Form
    {
        public frmEditor()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                StreamReader inputFile = new StreamReader(Application.StartupPath + "\\config.ini");
                mnuBoldFormat.Checked = Convert.ToBoolean(inputFile.ReadLine());
                mnuItalicFormat.Checked = Convert.ToBoolean(inputFile.ReadLine());
                mnuUnderlineFormat.Checked = Convert.ToBoolean(inputFile.ReadLine());

                int i = Convert.ToInt32(inputFile.ReadLine());
                switch (i)
                {
                    case 1:
                        mnuSmallSize.PerformClick();
                        break;
                    case 2:
                        mnuMediumSize.PerformClick();
                        break;
                    case 3:
                        mnuLargeSize.PerformClick();
                        break;
                }

                inputFile.Close();
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("Config file not found.", "Default reset",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
                mnuBoldFormat.Checked = false;
                mnuItalicFormat.Checked = false;
                mnuUnderlineFormat.Checked = false;
                mnuSmallSize.PerformClick();
            }
            ChangeFont();
        }

        private int fontSize = 8;
        private string fontName = "MS Sans Serif";

        public void ChangeFont()
        {
            FontStyle newFont;
            newFont = FontStyle.Regular;
            if (mnuBoldFormat.Checked)
            {
                newFont = newFont | FontStyle.Bold;
            }

            if (mnuItalicFormat.Checked)
            {
                newFont = newFont | FontStyle.Italic;
            }

            if (mnuUnderlineFormat.Checked)
            {
                newFont = newFont | FontStyle.Underline;
            }

            txtEditor.Font = new Font(fontName, fontSize, newFont);
        }

        private void mnuNewFile_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Are you sure you want to start a new file?", "New File",
                MessageBoxButtons.YesNo, MessageBoxIcon.Question,
                MessageBoxDefaultButton.Button2) == DialogResult.Yes)
            {
                txtEditor.Text = "";
            }
        }

        private void mnuExit_Click(object sender, EventArgs e)
        {

            if (MessageBox.Show("Are you sure you want to exit the program?", "New File",
                MessageBoxButtons.YesNo, MessageBoxIcon.Question,
                MessageBoxDefaultButton.Button2) == DialogResult.Yes)
            {
                Close();
            }
            else
            {
                return;
            }
        }

        private void mnuBoldFormat_Click(object sender, EventArgs e)
        {
            mnuBoldFormat.Checked = !mnuBoldFormat.Checked;
            ChangeFont();
        }

        private void mnuItalicFormat_Click(object sender, EventArgs e)
        {
            mnuItalicFormat.Checked = !mnuItalicFormat.Checked;
            ChangeFont();
        }

        private void mnuUnderlineFormat_Click(object sender, EventArgs e)
        {
            mnuUnderlineFormat.Checked = !mnuUnderlineFormat.Checked;
            ChangeFont();
        }

        private void mnuSizeFomat_Click(object sender, EventArgs e)
        {
            string SizeClicked = ((ToolStripMenuItem)sender).Text;
            mnuSmallSize.Checked = false;
            mnuMediumSize.Checked = false;
            mnuLargeSize.Checked = false;

            switch (SizeClicked)
            {
                case "&Small":
                    fontSize = 8;
                    mnuSmallSize.Checked = true;
                    break;
                case "&Medium":
                    fontSize = 12;
                    mnuMediumSize.Checked = true;
                    break;
                case "&Large":
                    fontSize = 18;
                    mnuLargeSize.Checked = true;
                    break;
            }

            ChangeFont();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            StreamWriter outputFile = new StreamWriter(Application.StartupPath + "\\config.ini");
            outputFile.WriteLine(mnuBoldFormat.Checked);
            outputFile.WriteLine(mnuItalicFormat.Checked);
            outputFile.WriteLine(mnuUnderlineFormat.Checked);
            if (mnuSmallSize.Checked)
                outputFile.WriteLine(1);
            else if (mnuMediumSize.Checked)
                outputFile.WriteLine(2);
            else
                outputFile.WriteLine(3);

            outputFile.Close();
        }

        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (dlgOpen.ShowDialog() == DialogResult.OK)
            {
                StreamReader inputFile = new StreamReader(dlgOpen.FileName);
                txtEditor.Text = inputFile.ReadToEnd();
                inputFile.Close();
                txtEditor.SelectionLength = 0;
            }
        }

        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            if (dlgSave.ShowDialog() == DialogResult.OK)
            {
                StreamWriter outputFile = new StreamWriter(dlgSave.FileName);
                outputFile.Write(txtEditor.Text);
                outputFile.Close();
            }
        }
    }
}