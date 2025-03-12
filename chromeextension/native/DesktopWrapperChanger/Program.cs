using System.Runtime.InteropServices;
using System.Text.Json;
using io.github.ba32107.Chrome.NativeMessaging;

class Program
{
    static void Main(string[] args)
    {
        NativeMessagingHost host = new();
        host.StartListening(message =>
        {
            var requestData = JsonSerializer.Deserialize<List<int>>(message);
            Desktop.SetBackground((byte)requestData[0], (byte)requestData[1], (byte)requestData[2]);
            return JsonSerializer.Serialize(new ResponseData
            {
                message = "ok"
            });
        });
    }
}
public class Desktop
{
    [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
    private static extern int SystemParametersInfo(int uAction, int uParm, string lpvParam, int fuWinIni);
    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern int SetSysColors(int cElements, int[] lpaElements, int[] lpRgbValues);

    public static void SetBackground(byte r, byte g, byte b)
    {
        int[] elements = { 1 };
        SystemParametersInfo(20, 0, "", 3);
        System.Drawing.Color color = System.Drawing.Color.FromArgb(r, g, b);
        int[] colors = { System.Drawing.ColorTranslator.ToWin32(color) };

        SetSysColors(elements.Length, elements, colors);
    }
}


class ResponseData
{
    public string message { get; set; }
}