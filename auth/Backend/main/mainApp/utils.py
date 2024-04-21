from .models import Nodes

def generate_fake_ip(operator):
    # Implementinging the logic for generating Fake IP based on the operator
    # using if-elif statements or a mapping dictionary
    if operator == 'Precall':
        # Check if there are available IPs in the range 172.16.156.x
        available_ips_156 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.156.{i}').exists()]

        if available_ips_156:
            return f'172.16.156.{available_ips_156[0]}'
        else:
            # If 172.16.156.x is full, check and allocate from 172.16.157.x
            available_ips_157 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.157.{i}').exists()]

            if available_ips_157:
                return f'172.16.157.{available_ips_157[0]}'
            else:
                raise ValueError('Cannot generate more Fake IP for Precall operator')

    elif operator == 'International':
        # Implementing logic for International operator (single range)
        available_ips_international = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.154.{i}').exists()]

        if available_ips_international:
            return f'172.16.154.{available_ips_international[0]}'
        else:
            raise ValueError('Cannot generate more Fake IP for International operator')

    elif operator == 'Enterprise/DWH':
        # Implementing logic for Enterprise/DWH operator (single range)
        available_ips_enterprise = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.152.{i}').exists()]

        if available_ips_enterprise:
            return f'172.16.152.{available_ips_enterprise[0]}'
        else:
            raise ValueError('Cannot generate more Fake IP for Enterprise/DWH operator')

    elif operator == 'Vodafone':
        # Check if there are available IPs in the range 172.16.160.x
        available_ips_vodafone = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Q(Fake_ip=f'172.16.160.{i}') | Q(Fake_ip=f'172.16.161.{i}')).exists()]

        if available_ips_vodafone:
            return f'172.16.160.{available_ips_vodafone[0]}'
        else:
            raise ValueError('Cannot generate more Fake IP for Vodafone operator')

    elif operator == 'Idea/WAP':
        # Check if there are available IPs in the ranges 172.16.163.x and 172.16.167.x
        available_ips_idea_wap_163 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.163.{i}').exists()]
        available_ips_idea_wap_167 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.167.{i}').exists()]

        if available_ips_idea_wap_163:
            return f'172.16.163.{available_ips_idea_wap_163[0]}'
        elif available_ips_idea_wap_167:
            return f'172.16.167.{available_ips_idea_wap_167[0]}'
        else:
            raise ValueError('Cannot generate more Fake IP for Idea/WAP operator')

    elif operator == 'Airtel':
        # Check if there are available IPs in the ranges 172.16.164.x and 172.16.165.x
        available_ips_airtel_164 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.164.{i}').exists()]
        available_ips_airtel_165 = [str(i) for i in range(2, 255) if not Nodes.objects.filter(Fake_ip=f'172.16.165.{i}').exists()]

        if available_ips_airtel_164:
            return f'172.16.164.{available_ips_airtel_164[0]}'
        elif available_ips_airtel_165:
            return f'172.16.165.{available_ips_airtel_165[0]}'
        else:
            raise ValueError('Cannot generate more Fake IP for Airtel operator')

    else:
        raise ValueError('Invalid operator')