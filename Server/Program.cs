using InTheHand.Net.Sockets;
using System;
using System.IO;
using System.Text;



namespace BluetoothServer
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Waiting for Token");
            string[] token = System.IO.File.ReadAllLines(@"C:\Users\daire\Desktop\QRCODEFILE.txt");
            foreach (string line in token) {}
           
            Guid guid = new Guid("B62C4E8D-62CC-404b-BBBF-BF3E3BBB1374");

            BluetoothListener Listener = new BluetoothListener(guid);
            Listener.Start();
            BluetoothClient connection = Listener.AcceptBluetoothClient();
            
            Stream mStream = connection.GetStream();
            while (true)
            {
                
                try
                {
                    byte[] received = new byte[36];
                    mStream.Read(received, 0, received.Length);


                    if ( token[0].Equals(Encoding.ASCII.GetString(received).ToString()))
                    {
                        Console.WriteLine("You are signed in!");
                        break;
                      
                    }
                    else
                    {
                        Console.WriteLine("You are NOT signed in!");
                        break;
                    }
                }
                catch (IOException exception)
                {
                    break;
                }   
            }
        }
    }
}
