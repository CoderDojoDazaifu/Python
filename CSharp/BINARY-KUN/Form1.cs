using System;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace BINARY_KUN
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "ファイルをドラッグ＆ドロップしてね。\n２進数で出力するよ。";
        }

        private void panel1_DragDrop(object sender, DragEventArgs e)
        {
            string[] fileNames = (string[])e.Data.GetData(DataFormats.FileDrop, false);

            StreamReader sr = new StreamReader(fileNames[0], Encoding.GetEncoding("utf-8"));
            string str = sr.ReadToEnd();
            sr.Close();

            int i = 0;
            label1.Text = "";
            foreach (Char c in str)
            {
                byte[] data = BitConverter.GetBytes(c);
                foreach (byte d in data)
                {
                    string s = Convert.ToString(d, 2).PadLeft(8, '0') + " ";
                    i += 9;
                    label1.Text += s;
                    if (i % 54 == 0)
                    {
                        label1.Text += "\r\n";
                    }
                }
            }
        }

        private void panel1_DragEnter(object sender, DragEventArgs e)
        {
            // File Only
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Copy;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }
    }
}
