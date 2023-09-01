namespace TextEditor
{
    partial class frmEditor
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            txtEditor = new TextBox();
            mnuMain = new MenuStrip();
            mnuFile = new ToolStripMenuItem();
            mnuNewFile = new ToolStripMenuItem();
            openToolStripMenuItem = new ToolStripMenuItem();
            saveToolStripMenuItem = new ToolStripMenuItem();
            mnuExit = new ToolStripMenuItem();
            mnuFormat = new ToolStripMenuItem();
            mnuBoldFormat = new ToolStripMenuItem();
            mnuItalicFormat = new ToolStripMenuItem();
            mnuUnderlineFormat = new ToolStripMenuItem();
            mnuSizeFormat = new ToolStripMenuItem();
            mnuSmallSize = new ToolStripMenuItem();
            mnuMediumSize = new ToolStripMenuItem();
            mnuLargeSize = new ToolStripMenuItem();
            dlgOpen = new OpenFileDialog();
            dlgSave = new SaveFileDialog();
            mnuMain.SuspendLayout();
            SuspendLayout();
            // 
            // txtEditor
            // 
            txtEditor.Location = new Point(12, 40);
            txtEditor.Multiline = true;
            txtEditor.Name = "txtEditor";
            txtEditor.ScrollBars = ScrollBars.Vertical;
            txtEditor.Size = new Size(597, 457);
            txtEditor.TabIndex = 0;
            // 
            // mnuMain
            // 
            mnuMain.ImageScalingSize = new Size(20, 20);
            mnuMain.Items.AddRange(new ToolStripItem[] { mnuFile, mnuFormat });
            mnuMain.Location = new Point(0, 0);
            mnuMain.Name = "mnuMain";
            mnuMain.Size = new Size(621, 28);
            mnuMain.TabIndex = 1;
            mnuMain.Text = "menuStrip1";
            // 
            // mnuFile
            // 
            mnuFile.DropDownItems.AddRange(new ToolStripItem[] { mnuNewFile, openToolStripMenuItem, saveToolStripMenuItem, mnuExit });
            mnuFile.Name = "mnuFile";
            mnuFile.Size = new Size(46, 24);
            mnuFile.Text = "&File";
            // 
            // mnuNewFile
            // 
            mnuNewFile.Name = "mnuNewFile";
            mnuNewFile.Size = new Size(128, 26);
            mnuNewFile.Text = "&New";
            mnuNewFile.Click += mnuNewFile_Click;
            // 
            // openToolStripMenuItem
            // 
            openToolStripMenuItem.Name = "openToolStripMenuItem";
            openToolStripMenuItem.Size = new Size(128, 26);
            openToolStripMenuItem.Text = "&Open";
            openToolStripMenuItem.Click += mnuFileOpen_Click;
            // 
            // saveToolStripMenuItem
            // 
            saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            saveToolStripMenuItem.Size = new Size(128, 26);
            saveToolStripMenuItem.Text = "&Save";
            saveToolStripMenuItem.Click += mnuFileSave_Click;
            // 
            // mnuExit
            // 
            mnuExit.Name = "mnuExit";
            mnuExit.Size = new Size(128, 26);
            mnuExit.Text = "E&xit";
            mnuExit.Click += mnuExit_Click;
            // 
            // mnuFormat
            // 
            mnuFormat.DropDownItems.AddRange(new ToolStripItem[] { mnuBoldFormat, mnuItalicFormat, mnuUnderlineFormat, mnuSizeFormat });
            mnuFormat.Name = "mnuFormat";
            mnuFormat.Size = new Size(70, 24);
            mnuFormat.Text = "F&ormat";
            // 
            // mnuBoldFormat
            // 
            mnuBoldFormat.Name = "mnuBoldFormat";
            mnuBoldFormat.Size = new Size(156, 26);
            mnuBoldFormat.Text = "&Bold";
            mnuBoldFormat.Click += mnuBoldFormat_Click;
            // 
            // mnuItalicFormat
            // 
            mnuItalicFormat.Name = "mnuItalicFormat";
            mnuItalicFormat.Size = new Size(156, 26);
            mnuItalicFormat.Text = "&Italic";
            mnuItalicFormat.Click += mnuItalicFormat_Click;
            // 
            // mnuUnderlineFormat
            // 
            mnuUnderlineFormat.Name = "mnuUnderlineFormat";
            mnuUnderlineFormat.Size = new Size(156, 26);
            mnuUnderlineFormat.Text = "&Underline";
            mnuUnderlineFormat.Click += mnuUnderlineFormat_Click;
            // 
            // mnuSizeFormat
            // 
            mnuSizeFormat.DropDownItems.AddRange(new ToolStripItem[] { mnuSmallSize, mnuMediumSize, mnuLargeSize });
            mnuSizeFormat.Name = "mnuSizeFormat";
            mnuSizeFormat.Size = new Size(156, 26);
            mnuSizeFormat.Text = "&Size";
            // 
            // mnuSmallSize
            // 
            mnuSmallSize.Checked = true;
            mnuSmallSize.CheckState = CheckState.Checked;
            mnuSmallSize.Name = "mnuSmallSize";
            mnuSmallSize.Size = new Size(147, 26);
            mnuSmallSize.Text = "&Small";
            mnuSmallSize.Click += mnuSizeFomat_Click;
            // 
            // mnuMediumSize
            // 
            mnuMediumSize.Name = "mnuMediumSize";
            mnuMediumSize.Size = new Size(147, 26);
            mnuMediumSize.Text = "&Medium";
            mnuMediumSize.Click += mnuSizeFomat_Click;
            // 
            // mnuLargeSize
            // 
            mnuLargeSize.Name = "mnuLargeSize";
            mnuLargeSize.Size = new Size(147, 26);
            mnuLargeSize.Text = "&Large";
            mnuLargeSize.Click += mnuSizeFomat_Click;
            // 
            // dlgOpen
            // 
            dlgOpen.Filter = "Text Files (*.txt)|*.txt";
            dlgOpen.Title = "Open File";
            // 
            // dlgSave
            // 
            dlgSave.Filter = "Text Files (*.txt)|*.txt";
            dlgSave.Title = "Save File";
            // 
            // frmEditor
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(621, 509);
            Controls.Add(txtEditor);
            Controls.Add(mnuMain);
            MainMenuStrip = mnuMain;
            Name = "frmEditor";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Text Editor";
            FormClosing += Form1_FormClosing;
            Load += Form1_Load;
            mnuMain.ResumeLayout(false);
            mnuMain.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox txtEditor;
        private MenuStrip mnuMain;
        private ToolStripMenuItem mnuFile;
        private ToolStripMenuItem mnuNewFile;
        private ToolStripMenuItem mnuExit;
        private ToolStripMenuItem mnuFormat;
        private ToolStripMenuItem mnuBoldFormat;
        private ToolStripMenuItem mnuItalicFormat;
        private ToolStripMenuItem mnuUnderlineFormat;
        private ToolStripMenuItem mnuSizeFormat;
        private ToolStripMenuItem mnuSmallSize;
        private ToolStripMenuItem mnuMediumSize;
        private ToolStripMenuItem mnuLargeSize;
        private ToolStripMenuItem openToolStripMenuItem;
        private ToolStripMenuItem saveToolStripMenuItem;
        private OpenFileDialog dlgOpen;
        private SaveFileDialog dlgSave;
    }
}