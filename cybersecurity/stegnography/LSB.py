import sys
import math
from os import path

import cv2
import numpy as np

# Embed secret in the n least significant bit.
# Lower n make picture less loss but lesser storage capacity.
BITS = 2

HIGH_BITS = 256 - (1 << BITS)
LOW_BITS = (1 << BITS) - 1
BYTES_PER_BYTE = math.ceil(8 / BITS)
FLAG = '%'


def insert(img_path, msg):
    img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)
    # Save origin shape to restore image
    ori_shape = img.shape
    print(ori_shape)
    max_bytes = ori_shape[0] * ori_shape[1] // BYTES_PER_BYTE
    # Encode message with length
    msg = '{}{}{}'.format(len(msg), FLAG, msg)
    assert max_bytes >= len(
        msg), "Message greater than capacity:{}".format(max_bytes)
    data = np.reshape(img, -1)
    for (idx, val) in enumerate(msg):
        encode(data[idx*BYTES_PER_BYTE: (idx+1) * BYTES_PER_BYTE], val)

    img = np.reshape(data, ori_shape)
    filename, _ = path.splitext(img_path)
    filename += '_lsb_embeded' + ".png"
    cv2.imwrite(filename, img)
    return filename

def encode(block, data):
    # returns the Unicode code from a given character
    data = ord(data)
    for idx in range(len(block)):
        block[idx] &= HIGH_BITS
        block[idx] |= (data >> (BITS * idx)) & LOW_BITS

if __name__ == '__main__':

    if len(sys.argv) == 3:
        img_path = sys.argv[1]
        msg = sys.argv[2]
    else:
        img_path = "./assets/man.jpeg"
        msg = """Below is a 2000-word highly confidential message that you can use for steganography:

---

**"Top-Secret Strategic Initiative"**

The information contained within this document is of the utmost sensitivity and should be handled with extreme caution. Unauthorized disclosure of any part of this message will result in immediate security breaches and could potentially compromise the entire operation. As such, this document is to be shared only with the highest level of clearance and must be encrypted during all forms of transmission and storage.

### **Overview of Operation Silent Shadow**

Operation Silent Shadow is an unprecedented initiative that has been classified at the highest level of secrecy. The primary objective of this operation is to secure and control key technological assets that are currently considered critical to national security. These assets are spread across various sectors, including cybersecurity, artificial intelligence, quantum computing, and advanced cryptography. The success of Operation Silent Shadow is contingent upon the ability to execute the plan with absolute precision and minimal exposure.

### **Phase 1: Intelligence Gathering**

The first phase of the operation involves the systematic gathering of intelligence related to potential threats and vulnerabilities associated with the targeted assets. This includes identifying all known adversaries, assessing their capabilities, and determining their level of interest in these assets. Advanced reconnaissance methods, including satellite surveillance, cyber espionage, and covert operations, will be employed to gather actionable intelligence. The intelligence gathered during this phase will be used to develop a comprehensive threat matrix that will guide the subsequent phases of the operation.

### **Phase 2: Asset Acquisition**

Upon completion of the intelligence-gathering phase, the operation will transition to the asset acquisition phase. This phase involves the discreet procurement of key technological assets identified in the threat matrix. A combination of legal and covert means will be used to acquire these assets. For assets that are currently in possession of foreign entities, a series of covert operations will be launched to retrieve them. These operations will be executed by elite units with specialized training in infiltration, extraction, and cyber operations. All actions taken during this phase must be untraceable and devoid of any evidence that could link them to Operation Silent Shadow.

### **Phase 3: Secure Containment**

Once the assets have been acquired, they will be transferred to secure containment facilities that have been specially constructed for this purpose. These facilities are located in remote, undisclosed locations and are equipped with state-of-the-art security measures, including biometric access controls, advanced surveillance systems, and AI-driven threat detection algorithms. The assets will be stored in environmentally controlled vaults that are designed to prevent tampering, unauthorized access, or environmental degradation. Regular security audits and drills will be conducted to ensure that the containment facilities remain impervious to all known forms of intrusion.

### **Phase 4: Technological Exploitation**

With the assets securely contained, the operation will enter the technological exploitation phase. During this phase, a select group of scientists, engineers, and analysts with the highest security clearance will be granted access to the assets. Their task will be to reverse-engineer the technologies, analyze their capabilities, and develop countermeasures that can be used to neutralize potential threats. This work will be conducted in isolated, high-security laboratories that are equipped with advanced research and development tools. All findings and discoveries made during this phase will be classified and stored in encrypted databases that are only accessible by authorized personnel.

### **Phase 5: Strategic Deployment**

The final phase of Operation Silent Shadow involves the strategic deployment of the technologies and countermeasures developed during the exploitation phase. This phase will be coordinated by a central command unit that has the authority to deploy resources as needed. The deployment will be carried out in a manner that minimizes exposure and maximizes impact. In cases where it is deemed necessary, the technologies may be weaponized and used as a deterrent against potential adversaries. Strict protocols will be in place to govern the use of these technologies, and any deviation from these protocols will be met with severe consequences.

### **Operational Security Protocols**

Throughout all phases of Operation Silent Shadow, stringent operational security protocols will be enforced to prevent leaks, sabotage, or unauthorized access. These protocols include, but are not limited to, the following:

1. **Compartmentalization:** All personnel involved in the operation will only have access to the information and assets necessary for their specific roles. No single individual will have access to the entire scope of the operation.
   
2. **Encryption:** All communications, documents, and data related to the operation will be encrypted using quantum-resistant encryption algorithms. Any attempt to decrypt this information without authorization will trigger an immediate security response.
   
3. **Surveillance and Monitoring:** Continuous surveillance and monitoring of all personnel, facilities, and communication channels will be conducted. Any anomalies or suspicious activities will be investigated immediately.
   
4. **Incident Response:** A rapid incident response team will be on standby at all times to address any security breaches or threats. This team is equipped with advanced cyber defense tools and has the authority to neutralize any perceived threats.

5. **Regular Audits:** Regular security audits will be conducted to identify any potential weaknesses in the operation. These audits will be performed by independent security experts who are not directly involved in the operation.

### **Contingency Plans**

Given the high stakes involved in Operation Silent Shadow, multiple contingency plans have been developed to address potential failures or unforeseen challenges. These contingency plans include:

1. **Data Destruction:** In the event that containment facilities are compromised, all sensitive data will be immediately destroyed using zero-trace data erasure methods. This will prevent adversaries from gaining access to classified information.

2. **Asset Relocation:** Should a containment facility be deemed unsafe, all assets will be rapidly relocated to an alternative secure location. This relocation will be conducted under the cover of darkness using secure, untraceable transport methods.

3. **False Flag Operations:** To mislead potential adversaries and protect the true nature of Operation Silent Shadow, false flag operations will be conducted. These operations will create the illusion of unrelated activities, diverting attention away from the operation's true objectives.

4. **Evacuation Protocols:** In the unlikely event of a catastrophic security breach, all personnel will be evacuated from the containment facilities and relocated to secure bunkers. These bunkers are equipped with supplies and communication tools that will allow personnel to continue their work in a secure environment.

### **Conclusion**

Operation Silent Shadow represents a critical initiative in the ongoing effort to secure key technological assets that are vital to national security. The success of this operation depends on the unwavering commitment to the security protocols outlined in this document. All personnel involved must exercise the highest level of discretion and professionalism in their roles. Any deviation from the protocols or unauthorized disclosure of information will be met with severe consequences, including legal action and loss of security clearance.

This document will self-destruct after reading, and all personnel are required to acknowledge their understanding of the contents before proceeding with their assigned tasks.

---

This message is designed to be sensitive and confidential, making it suitable for steganography purposes.   """
    
    res_path = insert(img_path, msg)
    print("Successfully embedded.")
